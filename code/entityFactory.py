#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        #encontre a ent
        match entity_name:
            #caso o nome do arquivo for  Level1Bg
            case 'Level1Bg':
                list_bg = [] #lista vazia
                #para cada dos 7 item em i
                for i in range(7):
                    #começara no 0
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    #e quando chegar no WIN_WIDTH
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                    #resetara a ordem de list
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
        return None
