# Cores
COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)

# Opções do Menu
MENU_OPTION = (
    'NEW GAME 1P',
    'NEW GAME 2P - COOPERATIVE',
    'NEW GAME 2P - COMPETITIVE',
    'SCORE',
    'EXIT'
)

# Dimensões da Janela
WIN_WIDTH = 576
WIN_HEIGHT = 324

# Velocidades do Parallax (Level 1)
# Quanto maior o número, mais rápido a camada se move (camadas da frente)
ENTITY_SPEED = {
    'level1Bg0': 0,  # Céu estático
    'level1Bg2': 1,  # Nuvens distantes
    'level1Bg3': 2,  # Montanhas
    'level1Bg4': 3,  # Árvores distantes
    'level1Bg5': 4,  # Árvores próximas
    'level1Bg6': 5,  # Gramado
    'level1Bg7': 6   # Elementos de primeiro plano
}