#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from menu import menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        print('Setup Start')
        print('Setup End')
        print('Loop Start')

        menu = Menu(self.window)
        menu.run()