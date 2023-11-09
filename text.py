# File:     text.py
# Purpose:  Creates the area for the text, as well as the text inside
# Author:   Brandon Short, bgs43
# Date:     8 November 2023

import pygame
from drawable import Drawable


class Text(Drawable):
    # Constructor
    def __init__(self, message="Pygame",  x=0, y=0, \
                 color=(0,0,0), size=24):
        super().__init__(x, y)
        self.__message = message
        self.__color = color
        self.__fontObj = pygame.font.Font("freesansbold.ttf", size)
    
    # Getters
    def draw(self, surface):
        self.__surface = self.__fontObj.render(self.__message, \
                                               True, self.__color)
        surface.blit(self.__surface, self.getLoc())

    def get_rect(self):
        return self.__surface.get_rect()
    
    # Setters
    def setMessage(self, message):
        self.__message = message
        