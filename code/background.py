#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple, speed_factor: float = 1.0):
        super().__init__(name, position)
        self.speed_factor = speed_factor

        if self.surf:
            self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
            self.rect = self.surf.get_rect(topleft=position)

    def move(self):
        # Cada camada se move com base no seu fator de velocidade
        self.rect.x -= max(1, int(2 * self.speed_factor))

        if self.rect.right <= 0:
            self.rect.x = WIN_WIDTH