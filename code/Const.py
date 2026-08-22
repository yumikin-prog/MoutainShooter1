import pygame

# C
COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)

# E
ENTITY_SPEED = {
    'level1Bg0': 0,
    'level1Bg1': 1,
    'level1Bg2': 2,
    'level1Bg3': 3,
    'level1Bg4': 4,
    'level1Bg5': 5,
    'level1Bg6': 6,
    'level1Bg7': 6,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1,
    'exhaust1': 6,        # Tiro do Player 1
    'exhaust35 (1)': 6,   # Tiro do Player 2 (luz verde)
}

# M
MENU_OPTION = (
    'NEW GAME 1P',
    'NEW GAME 2P - COOPERATIVE',
    'NEW GAME 2P - COMPETITIVE',
    'SCORE',
    'EXIT',
)

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}

# Player 1 atira no ESPAÇO | Player 2 atira no CTRL Esquerdo
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE, 'Player2': pygame.K_LCTRL}

WIN_WIDTH = 576
WIN_HEIGHT = 324
EVENT_ENEMY = pygame.USEREVENT + 1