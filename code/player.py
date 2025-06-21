#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
#from pygame.examples.audiocapture import names

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.entity import Entity
from code.playerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        #movimento do player y para cima/baixo e x para esq/dir
        #apos ser precionado a tecla | nao sera permitido passar do valor 0({> 0}superior e esquerdo{-y}) WIN_({< WIN_}inferior e direito{x}) da tela
        #e entao o valor de ENTITY_SPEED sera igual a negativo(-) ou positivo(+)[para o nome de qual Entity"Player1/Player2"] !nota: verificar a Const para ver suas interações do 'Player1'
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]


    def shoot(self, ):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                 return PlayerShot(f'{self.name}Shoot', (self.rect.centerx, self.rect.centery))
