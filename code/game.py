#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu

# classe para rodar o game
class Game:
    def __init__(self):
        #iniciar o pygame/fazer uma janela de visualizacao
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    # enquanto o game roda
    def run(self, ):
        #enquanto verdadeiro(o game rodar)
        while True:
            #chama o menu para rodar
            menu = Menu(self.window)
            menu_return = menu.run()
            #caso os escolhido do menu for o 0,1,2 levara ao level 1
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            #caso for a 4 saia do game
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                #futura score
                pass

