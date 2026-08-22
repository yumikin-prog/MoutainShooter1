#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, COLOR_YELLOW, COLOR_WHITE, COLOR_ORANGE


class Menu:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.menu_option = MENU_OPTION
        self.selected_index = 0

        try:
            self.bg = pygame.image.load('./asset/MenuBg.png').convert()
            self.bg = pygame.transform.scale(self.bg, (WIN_WIDTH, WIN_HEIGHT))
        except pygame.error:
            self.bg = None

    def run(self, main_screen=None):
        clock = pygame.time.Clock()

        for ext in ['.mp3', '.wav']:
            try:
                pygame.mixer.music.load(f'./asset/menu{ext}')
                pygame.mixer.music.play(-1)
                break
            except pygame.error:
                continue

        while True:
            clock.tick(60)

            if self.bg:
                self.window.blit(self.bg, (0, 0))
            else:
                self.window.fill((0, 0, 0))

            # Título do Jogo
            self.draw_text_center(24, "MOUNTAIN SHOOTER", COLOR_ORANGE, (WIN_WIDTH // 2, 35))

            # Opções de Seleção do Menu
            for i, option in enumerate(self.menu_option):
                color = COLOR_YELLOW if i == self.selected_index else COLOR_WHITE
                self.draw_text_center(14, option, color, (WIN_WIDTH // 2, 85 + i * 22))

            # Captura de Eventos de Navegação
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.menu_option)
                    elif event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.menu_option)
                    elif event.key == pygame.K_RETURN:
                        return self.menu_option[self.selected_index]
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            if main_screen:
                scaled = pygame.transform.scale(self.window, main_screen.get_size())
                main_screen.blit(scaled, (0, 0))
                pygame.display.flip()
            else:
                pygame.display.flip()

    def draw_text_center(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size, bold=True)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_pos)
        self.window.blit(text_surf, text_rect)