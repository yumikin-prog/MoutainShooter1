#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background
from code.enemy import Enemy
from code.player import Player
from code.entity import Entity


class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        if name == 'Player2Shot':
            try:
                self.surf = pygame.image.load('./asset/exhaust35 (3).png').convert_alpha()
            except Exception:
                try:
                    self.surf = pygame.image.load('./asset/Player1Shot.png').convert_alpha()
                except Exception:
                    pass

        self.rect = self.surf.get_rect(center=position)

    def move(self):
        self.rect.x += 8


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple = None):
        # LEVEL 1 - Parallax
        if entity_name in ['Level1Bg', 'Level1', 'LEVEL1']:
            bg_list = []
            for i in range(11):
                speed = 0.2 + (i * 0.15)
                bg1 = Background(f'level1Bg{i}', (0, 0), speed_factor=speed)
                bg2 = Background(f'level1Bg{i}', (WIN_WIDTH, 0), speed_factor=speed)
                bg_list.extend([bg1, bg2])
            return bg_list

        # LEVEL 2 - Parallax
        elif entity_name in ['Level2Bg', 'Level2', 'LEVEL2']:
            bg_list = []
            for i in range(7):
                speed = 0.2 + (i * 0.2)
                bg1 = Background(f'level2Bg{i}', (0, 0), speed_factor=speed)
                bg2 = Background(f'level2Bg{i}', (WIN_WIDTH, 0), speed_factor=speed)
                bg_list.extend([bg1, bg2])
            return bg_list

        # LEVEL 3 - Parallax completo preenchendo 100% da tela
        elif entity_name in ['Level3Bg', 'Level3', 'LEVEL3']:
            bg_list = []
            for i in range(5):
                speed = 0.15 + (i * 0.2)
                try:
                    bg1 = Background(f'level3Bg{i}', (0, 0), speed_factor=speed)
                    bg2 = Background(f'level3Bg{i}', (WIN_WIDTH, 0), speed_factor=speed)

                    # Ajusta escala para cobrir a altura total sem lacunas
                    bg1.surf = pygame.transform.scale(bg1.surf, (WIN_WIDTH, WIN_HEIGHT))
                    bg2.surf = pygame.transform.scale(bg2.surf, (WIN_WIDTH, WIN_HEIGHT))

                    bg_list.extend([bg1, bg2])
                except Exception:
                    pass
            return bg_list

        # Jogadores
        elif entity_name == 'Player1':
            return Player('Player1', (20, WIN_HEIGHT // 2))

        elif entity_name == 'Player2':
            return Player('Player2', (20, WIN_HEIGHT // 2 + 40))

        # Tiros
        elif 'Player' in entity_name and 'Shot' in entity_name:
            pos = position if position else (0, 0)
            return PlayerShot(entity_name, pos)

        # Inimigos
        elif entity_name in ['Enemy1', 'Enemy2', 'Enemy3']:
            rand_y = random.randint(40, WIN_HEIGHT - 60)
            rand_x = WIN_WIDTH + random.randint(10, 80)
            pos = position if position else (rand_x, rand_y)
            return Enemy(entity_name, pos)

        return None