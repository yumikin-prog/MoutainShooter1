#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pygame
from pygame.font import Font
from pygame import Surface, Rect
from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE


class Menu:

    def __init__(self, window):
        self.window = window

        # Descobre o caminho seguro até a pasta 'asset'
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Mude 'orig.png' para 'MenuBg.png' ou 'Menu.png' se você tiver renomeado a imagem
        image_path = os.path.join(base_dir, 'asset', 'orig.png')

        surf_original = pygame.image.load(image_path)
        self.surf = pygame.transform.scale(surf_original, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        music_path = os.path.join(base_dir, 'asset', 'Menu.mp3')

        if os.path.exists(music_path):
            pygame.mixer_music.load(music_path)
            pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            # Título do Jogo
            self.menu_text(50, "Mountain", COLOR_ORANGE, (WIN_WIDTH / 2, 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, (WIN_WIDTH / 2, 120))

            # Opções do Menu
            self.menu_text(20, "NEW GAME 1P", (255, 255, 255), (WIN_WIDTH / 2, 180))
            self.menu_text(20, "NEW GAME 2P - COOPERATIVE", (255, 255, 255), (WIN_WIDTH / 2, 210))
            self.menu_text(20, "NEW GAME 2P - COMPETITIVE", (255, 255, 255), (WIN_WIDTH / 2, 240))
            self.menu_text(20, "SCORE", (255, 255, 255), (WIN_WIDTH / 2, 270))
            self.menu_text(20, "EXIT", (255, 255, 255), (WIN_WIDTH / 2, 300))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)