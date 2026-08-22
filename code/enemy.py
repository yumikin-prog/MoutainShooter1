#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import pygame
from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.direction_x = -1  # -1 = avançar para a esquerda, 1 = recuar (ir para trás)
        self.direction_y = 1  # 1 = descer, -1 = subir
        self.speed_y = 2
        self.wave_counter = 0

    def move(self):
        speed_x = ENTITY_SPEED.get(self.name, 4)

        # Movimento do Enemy3 (Avança, recua e oscila de forma senoidal)
        if 'Enemy3' in self.name:
            self.wave_counter += 0.08

            current_speed_x = speed_x * 1.5 if self.direction_x == 1 else speed_x
            self.rect.x += current_speed_x * self.direction_x
            self.rect.y += math.sin(self.wave_counter) * 3

            if self.rect.left <= 80:
                self.direction_x = 1
            elif self.rect.right >= WIN_WIDTH - 20:
                self.direction_x = -1

            if self.rect.top < 10:
                self.rect.top = 10
            elif self.rect.bottom > WIN_HEIGHT - 10:
                self.rect.bottom = WIN_HEIGHT - 10

        # Movimento do Enemy1 e Enemy2 (Avançam para a esquerda enquanto sobem e descem)
        else:
            self.rect.x -= speed_x
            self.rect.y += self.speed_y * self.direction_y

            # Inverte a direção vertical ao bater nos limites superior/inferior da tela
            if self.rect.top <= 10:
                self.direction_y = 1
            elif self.rect.bottom >= WIN_HEIGHT - 10:
                self.direction_y = -1