#Consts
import pygame

#C
COLOR_ORANGE = (255, 127, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

#E
#adiciona +1 evento
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Level1Bg5': 5,
                'Level1Bg6': 6,
                'Player1': 3,
                'Player1Shoot': 7,
                'Player2': 3,
                'Player2Shoot': 7,
                'Enemy1': 2,
                'Enemy1Shoot': 7,
                'Enemy2': 1,
                'Enemy2Shoot': 5.5,
                }

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player1': 300,
    'Player1Shoot': 1,
    'Player2': 300,
    'Player2Shoot': 1,
    'Enemy1': 50,
    'Enemy1Shoot': 1,
    'Enemy2': 60,
    'Enemy2Shoot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player1': 15,
    'Player2': 15,
    'Enemy1': 70,
    'Enemy2': 55,
}


#K
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w }
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s }
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a }
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d }
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RSHIFT,
                    'Player2': pygame.K_LSHIFT}

#S
SPAWN_TIME = 4000

#M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOP',
               'NEW GAME 2P - COMP',
               'SCORE',
               'EXIT')

#T
TIMEOUT_LEVEL = 20000

#W
#tamanhos do background
WIN_WIDTH = 576
WIN_HEIGHT = 324


"""
    pos:0,0+---------------------------+
           |                           |
           |                           |
           |                           |
          Y|                           |
           |                           |
           |                           |
           |                           |
           +---------------------------+576,324
                         X
"""




