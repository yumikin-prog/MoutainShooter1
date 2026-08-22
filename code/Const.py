#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

WIN_WIDTH = 576
WIN_HEIGHT = 324

COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_ORANGE = (255, 165, 0)

MENU_OPTION = (
    'NEW GAME 1P',
    'NEW GAME 2P - COOPERATIVE',
    'NEW GAME 2P - COMPETITIVE',
    'SCORE / RANKING',
    'INSTRUCTIONS',
    'EXIT'
)

EVENT_ENEMY = 32770

ENTITY_SPEED = {
    'Player1': 6,
    'Player2': 6,
    'Enemy1': 4,
    'Enemy2': 3,
    'Enemy3': 3,
    'Player1Shot': 8,
    'Player2Shot': 8,
    'Enemy1Shot': 5,
    'Enemy2Shot': 5,
    'Enemy3Shot': 5,
}

ENTITY_HEALTH = {
    'Level1Bg': 999,
    'Level2Bg': 999,
    'Level3Bg': 999,
    'Player1': 5,
    'Player2': 5,
    'Enemy1': 1,
    'Enemy2': 2,
    'Enemy3': 3,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'Enemy3Shot': 1,
}

ENTITY_DAMAGE = {
    'Player1': 1,
    'Player2': 1,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'Enemy3Shot': 1,
}

PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}