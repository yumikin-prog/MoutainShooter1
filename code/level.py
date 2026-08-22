#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import pygame

from code.Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, EVENT_ENEMY
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.eventManager import EventManager, ScoreHUD
from code.player import Player
from code.playerShot import PlayerShot


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))

        if self.game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        # Cria inimigos iniciais
        self.entity_list.append(EntityFactory.get_entity('Enemy1'))
        self.entity_list.append(EntityFactory.get_entity('Enemy2'))

        # Timer nativo do Pygame para criar novos inimigos a cada 2000ms (2s)
        pygame.time.set_timer(EVENT_ENEMY, 2000)

        self.timeout = 20000

        self.event_manager = EventManager()
        self.score_hud = ScoreHUD()
        self.event_manager.inscrever(self.score_hud)

    def checar_interacoes_mediator(self):
        # 1. Tiro disparado da ponta da nave
        for ent in self.entity_list:
            if isinstance(ent, Player) and ent.shoot():
                shot_pos = (ent.rect.right, ent.rect.centery)
                self.entity_list.append(EntityFactory.get_entity(f'{ent.name}Shot', shot_pos))

        # 2. Colisão: Projétil -> Inimigo
        for ent1 in list(self.entity_list):
            if isinstance(ent1, PlayerShot):
                for ent2 in list(self.entity_list):
                    if isinstance(ent2, Enemy) and ent1.rect.colliderect(ent2.rect):
                        if ent1 in self.entity_list:
                            self.entity_list.remove(ent1)
                        if ent2 in self.entity_list:
                            self.entity_list.remove(ent2)

            # 3. Colisão: Player -> Inimigo
            if isinstance(ent1, Player):
                for ent2 in list(self.entity_list):
                    if isinstance(ent2, Enemy) and ent1.rect.colliderect(ent2.rect):
                        self.entity_list.remove(ent1)
                        self.exibir_game_over()
                        return False

            # 4. Remove tiro que saiu pela direita ou inimigo que saiu pela esquerda
            if isinstance(ent1, Enemy) and ent1.rect.right < 0:
                if ent1 in self.entity_list:
                    self.entity_list.remove(ent1)
            elif isinstance(ent1, PlayerShot) and ent1.rect.left > WIN_WIDTH:
                if ent1 in self.entity_list:
                    self.entity_list.remove(ent1)

        # Se não houver nenhum jogador vivo na lista de entidades
        players = [e for e in self.entity_list if isinstance(e, Player)]
        if not players:
            self.exibir_game_over()
            return False

        return True

    def exibir_game_over(self):
        """Desenha a mensagem 'VOCÊ PERDEU!' em branco por cima do fundo do jogo."""
        # Redesenha todas as entidades restantes (fundo e elementos) para manter a tela visível
        for ent in self.entity_list:
            self.window.blit(source=ent.surf, dest=ent.rect)

        # Configura o texto em BRANCO
        font = pygame.font.SysFont("Lucida Sans Typewriter", 40, bold=True)
        text_surf = font.render("VOCÊ PERDEU!", True, COLOR_WHITE)
        text_rect = text_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))

        self.window.blit(text_surf, text_rect)
        pygame.display.flip()

        # Interrompe a música ao perder
        pygame.mixer.music.stop()

        # Aguarda 2 segundos com o texto em branco sobre as árvores
        pygame.time.delay(2000)

    def run(self):
        nome_limpo = self.name.lower()
        extensoes = ['.mp3', '.MP3', '.wav', '.WAV']

        musica_carregada = False
        for ext in extensoes:
            caminho = f'./asset/{nome_limpo}{ext}'
            try:
                pygame.mixer.music.load(caminho)
                pygame.mixer.music.play(-1)
                musica_carregada = True
                break
            except pygame.error:
                continue

        if not musica_carregada:
            print(f"[AVISO] Música ./asset/{nome_limpo}.mp3 não encontrada.")

        clock = pygame.time.Clock()

        playing = True
        while playing:
            clock.tick(60)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # Executa a checagem das interações e verifica se o jogo continua
            playing = self.checar_interacoes_mediator()
            if not playing:
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    enemy_name = random.choice(['Enemy1', 'Enemy2'])
                    self.entity_list.append(EntityFactory.get_entity(enemy_name))

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)