#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background
from code.enemy import Enemy
from code.player import Player
from code.playerShot import PlayerShot


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in [0, 2, 3, 4, 5, 6, 7]:
                    list_bg.append(Background(f'level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                y_pos = random.randint(40, WIN_HEIGHT - 40)
                enemy = Enemy('Enemy1', (0, 0))
                enemy.rect.center = (WIN_WIDTH + 20, y_pos)
                return enemy
            case 'Enemy2':
                y_pos = random.randint(40, WIN_HEIGHT - 40)
                enemy = Enemy('Enemy2', (0, 0))
                enemy.rect.center = (WIN_WIDTH + 20, y_pos)
                return enemy
            case 'Player1Shot':
                # Tiro do Player 1: exhaust1.png
                return PlayerShot('exhaust1', position)
            case 'Player2Shot':
                # Tiro do Player 2: exhaust35 (1).png (luz verde)
                return PlayerShot('exhaust35 (1)', position)

        return None