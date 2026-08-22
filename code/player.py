#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, WIN_WIDTH, WIN_HEIGHT
from code.entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = 0

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= 3
        if pressed_keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += 3
        if pressed_keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= 3
        if pressed_keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += 3

        if self.shot_delay > 0:
            self.shot_delay -= 1

    def shoot(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[PLAYER_KEY_SHOOT[self.name]] and self.shot_delay == 0:
            self.shot_delay = 12
            return True
        return False