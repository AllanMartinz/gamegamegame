#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from code.Const import ENTITY_HEALTH


#classe abstrata para que possa ser usada como pai
class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        #carregar carrega as imagem apartir do name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        #velocidade
        self.speed = 0
        #vida
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self, ):
        pass
