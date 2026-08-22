#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Dict, Any, List
import sys
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, COLOR_YELLOW
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        # Inicia com janela redimensionável no tamanho padrão
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Mountain Shooter")
        self.is_fullscreen = False

    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        if self.is_fullscreen:
            self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_option = menu.run()

            if menu_option == 'EXIT':
                pygame.quit()
                break

            elif menu_option in ['NEW GAME 1P', 'NEW GAME 2P - COOPERATIVE', 'NEW GAME 2P - COMPETITIVE']:
                self.start_level_flow(menu_option)

            elif menu_option == 'SCORE / RANKING':
                self.show_score_screen()

            elif menu_option == 'INSTRUCTIONS':
                self.show_instructions_screen()

    def show_instructions_screen(self):
        font_title = pygame.font.SysFont("Lucida Console", 28)
        font_text = pygame.font.SysFont("Lucida Console", 14)

        waiting = True
        clock = pygame.time.Clock()

        instructions = [
            "INSTRUCOES DO JOGO",
            "",
            "PLAYER 1:",
            "  - Movimento: Setas (Cima, Baixo, Esquerda, Direita)",
            "  - Atirar: Barra de Espaco",
            "",
            "PLAYER 2:",
            "  - Movimento: Teclas W, A, S, D",
            "  - Atirar: L-CTRL ou R-CTRL",
            "",
            "OBJETIVO:",
            "  - Sobreviva ate o tempo de cada fase acabar",
            "  - Destrua as naves inimigas e desvie dos ataques",
            "",
            "Pressione qualquer tecla para voltar ao Menu"
        ]

        while waiting:
            clock.tick(30)

            virtual_surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
            virtual_surface.fill((15, 25, 45))

            y_offset = 20
            for i, line in enumerate(instructions):
                if i == 0:
                    surf = font_title.render(line, True, COLOR_YELLOW)
                elif "PLAYER" in line or "OBJETIVO:" in line:
                    surf = font_text.render(line, True, COLOR_YELLOW)
                else:
                    surf = font_text.render(line, True, COLOR_WHITE)

                rect = surf.get_rect(center=(WIN_WIDTH // 2, y_offset))
                virtual_surface.blit(surf, rect)
                y_offset += 18 if i != 0 else 30

            scaled_surface = pygame.transform.scale(virtual_surface, self.window.get_size())
            self.window.blit(scaled_surface, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        self.toggle_fullscreen()
                    else:
                        waiting = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

    def show_score_screen(self):
        font_title = pygame.font.SysFont("Lucida Console", 28)
        font_text = pygame.font.SysFont("Lucida Console", 16)

        waiting = True
        clock = pygame.time.Clock()

        # Ranking estático demonstrativo/exemplo
        ranking = [
            "RANKING / TOP SCORES",
            "",
            "1. P1 MASTER - 15000 PTS",
            "2. ACE PILOT - 12000 PTS",
            "3. STAR HAWK - 09500 PTS",
            "4. CO-OP TEAM - 08000 PTS",
            "5. NOOB SHIP  - 02000 PTS",
            "",
            "Pressione qualquer tecla para voltar ao Menu"
        ]

        while waiting:
            clock.tick(30)

            virtual_surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
            virtual_surface.fill((25, 15, 35))

            y_offset = 40
            for i, line in enumerate(ranking):
                if i == 0:
                    surf = font_title.render(line, True, COLOR_YELLOW)
                else:
                    surf = font_text.render(line, True, COLOR_WHITE)

                rect = surf.get_rect(center=(WIN_WIDTH // 2, y_offset))
                virtual_surface.blit(surf, rect)
                y_offset += 25 if i != 0 else 40

            scaled_surface = pygame.transform.scale(virtual_surface, self.window.get_size())
            self.window.blit(scaled_surface, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        self.toggle_fullscreen()
                    else:
                        waiting = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

    def show_win_screen(self, p1_health: int, p2_health: int, game_mode: str):
        font_large = pygame.font.SysFont("Lucida Console", 36)
        font_small = pygame.font.SysFont("Lucida Console", 20)

        waiting = True
        clock = pygame.time.Clock()

        while waiting:
            clock.tick(30)

            virtual_surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
            virtual_surface.fill((10, 20, 40))

            title_surf = font_large.render("YOU WIN!", True, COLOR_YELLOW)
            title_rect = title_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 3))
            virtual_surface.blit(title_surf, title_rect)

            score_msg = f"P1 sobrou com {p1_health} HP"
            if game_mode in ['NEW GAME 2P - COOPERATIVE', 'NEW GAME 2P - COMPETITIVE']:
                score_msg += f" | P2 sobrou com {p2_health} HP"

            score_surf = font_small.render(score_msg, True, COLOR_WHITE)
            score_rect = score_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
            virtual_surface.blit(score_surf, score_rect)

            press_surf = font_small.render("Pressione qualquer tecla para voltar ao Menu", True, COLOR_WHITE)
            press_rect = press_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 60))
            virtual_surface.blit(press_surf, press_rect)

            scaled_surface = pygame.transform.scale(virtual_surface, self.window.get_size())
            self.window.blit(scaled_surface, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        self.toggle_fullscreen()
                    else:
                        waiting = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

    def start_level_flow(self, game_mode: str):
        levels: List[Dict[str, Any]] = [
            {'name': 'Level1', 'spawn_rate': 800, 'timeout': 20000},
            {'name': 'Level2', 'spawn_rate': 600, 'timeout': 20000},
            {'name': 'Level3', 'spawn_rate': 400, 'timeout': 20000},
        ]

        p1_health = 5
        p2_health = 5
        game_cleared = True

        for lvl_info in levels:
            lvl_name: str = str(lvl_info['name'])
            spawn_rate: int = int(lvl_info['spawn_rate'])
            timeout: int = int(lvl_info['timeout'])

            level = Level(
                window=self.window,
                name=lvl_name,
                game_mode=game_mode,
                spawn_rate=spawn_rate,
                timeout=timeout,
                p1_health=p1_health,
                p2_health=p2_health
            )

            success, p1_health, p2_health = level.run(self.window)

            if not success:
                game_cleared = False
                break

        if game_cleared:
            self.show_win_screen(p1_health, p2_health, game_mode)