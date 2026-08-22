#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import pygame

from code.Const import COLOR_WHITE, EVENT_ENEMY, WIN_WIDTH, WIN_HEIGHT
from code.entityFactory import EntityFactory
from code.entitymediator import EntityMediator
from code.player import Player


class Level:
    def __init__(self, window: pygame.Surface, name: str, game_mode: str, spawn_rate: int = 800, timeout: int = 20000, p1_health: int = 5, p2_health: int = 5):
        self.window = window
        self.virtual_surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.name = name
        self.game_mode = game_mode
        self.spawn_rate = spawn_rate
        self.timeout = timeout
        self.entity_list = []

        if '1' in self.name:
            self.enemy_pool = ["Enemy1", "Enemy2"]
        elif '2' in self.name:
            self.enemy_pool = ["Enemy1", "Enemy2"]
        else:
            self.enemy_pool = ["Enemy1", "Enemy2", "Enemy3"]

        bg_entities = EntityFactory.get_entity(f"{self.name}Bg")
        if bg_entities:
            if isinstance(bg_entities, list):
                self.entity_list.extend(bg_entities)
            else:
                self.entity_list.append(bg_entities)

        if p1_health > 0:
            p1 = EntityFactory.get_entity("Player1")
            self.player1 = p1 if isinstance(p1, Player) else None
            if self.player1:
                self.player1.health = p1_health
                self.entity_list.append(self.player1)
        else:
            self.player1 = None

        if self.game_mode in ["NEW GAME 2P - COOPERATIVE", "NEW GAME 2P - COMPETITIVE"] and p2_health > 0:
            p2 = EntityFactory.get_entity("Player2")
            self.player2 = p2 if isinstance(p2, Player) else None
            if self.player2:
                self.player2.health = p2_health
                self.entity_list.append(self.player2)
        else:
            self.player2 = None

        pygame.time.set_timer(EVENT_ENEMY, self.spawn_rate)
        self.font = pygame.font.SysFont("Lucida Console", 16)
        self.clock = pygame.time.Clock()

    def run(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], pygame.Surface):
            self.window = args[0]

        try:
            pygame.mixer.music.load(f"./asset/{self.name}.mp3")
            pygame.mixer.music.play(-1)
        except pygame.error:
            pass

        level_running = True
        start_ticks = pygame.time.get_ticks()

        while level_running:
            self.clock.tick(60)

            elapsed_time = pygame.time.get_ticks() - start_ticks
            time_left = max(0, (self.timeout - elapsed_time) // 1000)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    enemy_type = random.choice(self.enemy_pool)
                    new_enemy = EntityFactory.get_entity(enemy_type)
                    if new_enemy:
                        self.entity_list.append(new_enemy)

            for ent in list(self.entity_list):
                if isinstance(ent, Player):
                    if ent.shoot():
                        shot_pos = ent.get_shot_position()
                        shot = EntityFactory.get_entity(f"{ent.name}Shot", shot_pos)
                        if shot:
                            self.entity_list.append(shot)

            for ent in self.entity_list:
                ent.move()

            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            # DESENHA NA SUPERFÍCIE VIRTUAL (576x324)
            self.virtual_surface.fill((0, 0, 0))

            for ent in self.entity_list:
                self.virtual_surface.blit(ent.surf, ent.rect)

            p1_h = self.player1.health if (self.player1 and self.player1.health > 0) else 0
            p2_h = self.player2.health if (self.player2 and self.player2.health > 0) else 0

            hud_text = f"{self.name} - Tempo: {time_left}s | P1: {p1_h}"
            if self.game_mode in ["NEW GAME 2P - COOPERATIVE", "NEW GAME 2P - COMPETITIVE"]:
                hud_text += f" | P2: {p2_h}"

            txt_surf = self.font.render(hud_text, True, COLOR_WHITE)
            self.virtual_surface.blit(txt_surf, (10, 10))

            # ESCALA E DESENHA NA JANELA PRINCIPAL (Eles preenchem 100% da tela maximizada)
            scaled_surf = pygame.transform.scale(self.virtual_surface, self.window.get_size())
            self.window.blit(scaled_surf, (0, 0))

            pygame.display.flip()

            p1_dead = self.player1 is None or self.player1.health <= 0
            p2_dead = self.player2 is None or self.player2.health <= 0

            if elapsed_time >= self.timeout:
                pygame.mixer.music.stop()
                return True, p1_h, p2_h

            if self.game_mode in ["NEW GAME 2P - COOPERATIVE", "NEW GAME 2P - COMPETITIVE"]:
                if p1_dead and p2_dead:
                    pygame.mixer.music.stop()
                    return False, 0, 0
            else:
                if p1_dead:
                    pygame.mixer.music.stop()
                    return False, 0, 0

        pygame.mixer.music.stop()
        return True, p1_h, p2_h