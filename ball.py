# File:     ball.py
# Purpose:  Create the ball used for the game to break the bricks
# Author:   Brandon Short, bgs43
# Date:     8 November 2023

import pygame
from drawable import Drawable


class Ball(Drawable):
    # Constructor
    def __init__(self, x=0, y=0, radius=5, color=(0,0,0)):
        super().__init__(x, y)
        self.__color = color
        self.__radius = radius
        self.__xSpeed = 4
        self.__ySpeed = 4

    # Getters
    def getColor(self):
        return self.__color
    
    def getRadius(self): 
        return self.__radius
    
    def getXSpeed(self): 
        return self.__xSpeed
    
    def getYSpeed(self):
        return self.__ySpeed

    # Draw function
    def draw(self, surface):
        if self.isVisible():
            pygame.draw.circle(surface, self.__color, \
                               self.getLoc(), self.__radius)
    
    # Moving the ball
    def move(self):
        # Increase __x and __y by some amount
        currentX, currentY = self.getLoc()
        newX = currentX + self.__xSpeed
        newY = currentY + self.__ySpeed
        self.setX(newX)
        self.setY(newY)

        surface = pygame.display.get_surface()
        width, height = surface.get_size()

        if newX <= self.__radius or newX + self.__radius >= width:
            self.__xSpeed *= -1
        
        if newY <= self.__radius or newY + self.__radius >= height:
            self.__ySpeed *= -1

    def get_rect(self):
        location = self.getLoc()
        radius = self.__radius
        return pygame.Rect(location[0] - radius, location[1] - radius, \
                           2 * radius, 2 * radius)

    # Setters
    def setColor(self, color):
        self.__color = color

    def setRadius(self, radius): 
        self.__radius = radius

    def setXSpeed(self, speed): 
        self.__xSpeed = speed

    def setYSpeed(self, speed): 
        self.__ySpeed = speed

    def isTouchingBall(self, other):
        gameBall = self.get_rect()
        otherObj = other.get_rect()
        if (gameBall.x < otherObj.x + otherObj.width) and \
            (gameBall.x + gameBall.width > otherObj.x) and \
            (gameBall.y < otherObj.y + otherObj.height) and \
            (gameBall.height + gameBall.y > otherObj.y):
            return True
        return False

