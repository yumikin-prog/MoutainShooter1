#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


class Entity:
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.health = 1

        try:
            loaded_surf = pygame.image.load(f'./asset/{name}.png').convert_alpha()
            # Redimensionamento preventivo se o sprite do inimigo ultrapassar a dimensão normal
            if 'Enemy' in name and (loaded_surf.get_width() > 100 or loaded_surf.get_height() > 100):
                self.surf = pygame.transform.scale(loaded_surf, (64, 32))
            else:
                self.surf = loaded_surf
        except Exception:
            try:
                if 'Enemy' in name:
                    self.surf = pygame.image.load('./asset/Enemy1.png').convert_alpha()
                else:
                    self.surf = pygame.Surface((32, 32), pygame.SRCALPHA)
            except Exception:
                self.surf = pygame.Surface((32, 32), pygame.SRCALPHA)

        self.rect = self.surf.get_rect(topleft=position)

    def move(self):
        pass