# File:     brickBuilder.py
# Purpose:  Creates the bricks in the field
# Author:   Brandon Short, bgs43
# Date:     8 November 2023

import pygame
from drawable import Drawable

class Brick(Drawable): 
    # Constructor
    def __init__(self, x=0, y=0, width=40, height=15, color=(255,138,138)): 
        super().__init__(x, y)
        self.__width, self.__height = width, height 
        self.__color = color 
        self.__brickRect = pygame.Rect(x, y, self.__width, self.__height) 
    
    # Getters
    def get_rect(self):
        return self.__brickRect
    
    def getColor(self):
        return self.__color
    
    # Setters
    def draw(self, surface): 
        pygame.draw.rect(surface, self.__color, self.__brickRect)
             
    
    