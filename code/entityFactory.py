#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH
from code.background import Background


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
        return None
