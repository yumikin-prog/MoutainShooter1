#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Define a velocidade com base no nome do arquivo
        self.speed = ENTITY_SPEED.get(name, 1)

    def move(self):
        self.rect.x -= self.speed
        # Quando sai totalmente da tela à esquerda, volta para o lado direito
        if self.rect.right <= 0:
            self.rect.x = WIN_WIDTH