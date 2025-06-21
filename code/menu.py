#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Rect, Surface
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, C_WHITE, MENU_OPTION, C_YELLOW


#classe menu
class Menu:
    #ele chamara a window/ caregara a imagem do background/ e colocara a imagem no canto da imagem
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    #enquanto roda
    def run(self, ):
        #atribuicao ao menu onde deve comecar
        menu_option = 0
        #caregara a musica
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        #enquanto verdadeiro(o game rodar)/ mostrará o texto no menu/ para cada item em MENU_OPTION ira adicionar 25px de distancia do 200px
        while True:
            #DRAW IMAGES
            self.window.blit(self.surf, self.rect)
            self.menu_text(50, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                #menu_option sera igual a i o numero que for escolhido pelo menu_option sera pintado de amarelo caso não é de branco
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            # CHECK FOR ALL EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                #se ocorrer o evento de abaixar a tecla/ e ela for a seta para baixo ira acrescentar +1 no menu_option e checa ate no leght de MENU_OPTION
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: #DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: #UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: #ENTER KEY
                        return MENU_OPTION[menu_option]

    #texto usado
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)