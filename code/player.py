#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, ENTITY_SPEED
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = 0

    def move(self):
        pressed_key = pygame.key.get_pressed()
        speed = ENTITY_SPEED.get(self.name, 6)

        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= speed
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += speed
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= speed
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += speed

    def shoot(self):
        self.shot_delay -= 1
        pressed_key = pygame.key.get_pressed()

        if self.name == 'Player1':
            is_shooting = pressed_key[pygame.K_SPACE]
        else:
            is_shooting = pressed_key[pygame.K_LCTRL] or pressed_key[pygame.K_RCTRL]

        if is_shooting and self.shot_delay <= 0:
            self.shot_delay = 12
            return True
        return False

    def get_shot_position(self):
        # Alinhamento exato no bico/meio horizontal e vertical da nave
        return (self.rect.right, self.rect.centery)