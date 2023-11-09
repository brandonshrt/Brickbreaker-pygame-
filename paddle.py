# File:     paddle.py
# Purpose:  Creates the paddle that the ball bounces off of
# Author:   Brandon Short, bgs43
# Date:     8 November 2023

import pygame
from drawable import Drawable


class Paddle(Drawable):
    # Constructor
    def __init__(self, width, height, color):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        super().__init__(screenWidth/2, screenHeight/2)
        self.__color = color
        self.__width = width
        self.__height = height

    # Getters
    def draw(self, surface):
        pygame.draw.rect(surface, self.__color, self.get_rect())

    def get_rect(self):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        mouseX = pygame.mouse.get_pos()[0]
        return pygame.Rect(mouseX - self.__width/2, \
                           screenHeight - 20 - (self.__height), \
                            self.__width, \
                            self.__height)