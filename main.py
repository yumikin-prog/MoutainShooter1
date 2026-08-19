#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


class menu :

    def __init__(self, window):
        self.window = window

    def run(self):
        # O loop do menu deve estar AQUI dentro
        menu_option = True
        while menu_option:
            # 1. Preenche a tela com uma cor (ex: preta)
            self.window.fill((0, 0, 0))

            # 2. Atualiza a tela para ela de fato aparecer
            pygame.display.flip()

            # 3. Processa eventos (como fechar a janela)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting...')
                    pygame.quit()  # Encerra o Pygame
                    quit()  # Encerra o script Python