# File:     hw4.py
# Purpose:  Main script that runs the game using the created classes
# Author:   Brandon Short, bgs43
# Date:     8 November 2023

import pygame
from brickBuilder import Brick
from ball import Ball
from paddle import Paddle
from text import Text
import random

# Creating the window
pygame.init()
surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("HW4 Brick Breaker")

# Colors
black = (0,0,0)
red = (255,138,138)
purple = (197,179,245)
darkGreen = (42,87,54)
gold = (255,233,135)
platinum = (242,245,255)

# Creating the ball and paddle
myBall = Ball(400, 300, 15, black)
myPaddle = Paddle(150, 20, black)

# Creating the scorebaord and lives
myScoreboard = Text("Score: 0", 10, 10, darkGreen, 18)
myLives = Text("Lives: 3", 130, 10, darkGreen, 18)

# Creating the win and loss text
lose = Text("You lost!", 175, 250, (255,0,0), 100)
win = Text("You Win!", 175, 250, (0,255,0), 100)
quit = Text("'Q' to Quit", 330, 350, (0,0,0), 20)

# Setting the score to 0 and lives to 3
score = 0
lives = 3
i = 0

# Creating an empty list for the bricks
brickList = []
# Creates 5 initial bricks, varying in color (either purple or red)
while i < 5:
    color = purple
    if random.randint(1,5) == 1:
        color = red
    brickList.append(Brick(random.randint(20,800), random.randint(40,300), 25, 25, color))
    brickList[0].draw(surface) # Drawing the first brick on the screen
    i += 1

fpsClock = pygame.time.Clock()
running = True

# Starting the game
while running:
    # Creating the environment and populating it
    surface.fill((216,250,219))
    myBall.draw(surface)
    myPaddle.draw(surface)
    myScoreboard.draw(surface)
    myLives.draw(surface)
    
    # Ball bouncing off the paddle
    if myBall.intersects(myPaddle):
        myBall.setYSpeed(myBall.getYSpeed()*(-1))
        # Creating different bricks (bad, special, and normal)
        if random.randint(1,5) == 1: 
            brickList.append(Brick(random.randint(20,800), random.randint(40,300),\
                                    random.randint(25,35), random.randint(25,45), red))
            brickList[-1].draw(surface)
        elif random.randint(1,100) == 1:
            brickList.append(Brick(random.randint(20,800), random.randint(40,300),\
                                    random.randint(15,20), random.randint(15,20), gold))
            brickList[-1].draw(surface)
        elif random.randint(1,1000) == 1:
            brickList.append(Brick(random.randint(20,800), random.randint(40,300),\
                                    random.randint(5,10), random.randint(5,10), platinum))
            brickList[-1].draw(surface)
        else: 
            brickList.append(Brick(random.randint(20,800), random.randint(40,300),\
                                    random.randint(25,35), random.randint(25,45), purple))
            brickList[-1].draw(surface)
    
    # Ball intersecting with the bricks
    for brick in brickList:
        brick.draw(surface)
        if myBall.intersects(brick):
            # If the ball intersects will a red (bad) ball the user loses 5 points
            if brick.getColor() == (255,138,138): 
                score -= 5
                myScoreboard.setMessage(f"Score: {score}")
                brickList.remove(brick)
                myBall.setYSpeed(myBall.getYSpeed()*(-1))
            else: # Ball intersects with purple or gold brick
                if brick.getColor() == (197,179,245): # Purple brick adds 5 points
                    score += 5
                    myScoreboard.setMessage(f"Score: {score}")
                    brickList.remove(brick)
                    myBall.setYSpeed(myBall.getYSpeed()*(-1))
                elif brick.getColor() == (255,233,135): # Gold brick add 15 points
                    score += 15
                    myScoreboard.setMessage(f"Score: {score}")
                    brickList.remove(brick)
                    myBall.setYSpeed(myBall.getYSpeed()*(-1))
                elif brick.getColor() == (242,245,255): # Platinum brick add 50 points
                    score += 50
                    myScoreboard.setMessage(f"Score: {score}")
                    brickList.remove(brick)
                    myBall.setYSpeed(myBall.getYSpeed()*(-1))

    # The ball hits the bottom and the game stops
    if myBall.getLoc()[1] >= 585:
        myBall = Ball(400, 300, 15, black)
        lives -= 1
        myLives.setMessage(f"Lives: {lives}")
        myBall.__x, myBall.__y = 20, 70

    # Lost all lives
    if lives <= 0:
        surface.fill((216,250,219))
        quit.draw(surface)
        lose.draw(surface)

    # Win the game
    if score >= 300:
        surface.fill((216,250,219))
        quit.draw(surface)
        win.draw(surface)

    # Score below zero
    if score < 0:
        surface.fill((216,250,219))
        quit.draw(surface)
        lose.draw(surface)

    # Ball movement
    myBall.move()

    # Quitting the game
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or \
            (event.type == pygame.KEYDOWN and \
             event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            myBall.setVisible(not myBall.isVisible())

    # Update the screen
    pygame.display.update()
    fpsClock.tick(60)


