'''
    ---------------------------------------------------------------------------------------
    Joshua Peck and Grant Schowalter Official Prototype Release **Pencil E-Racers** v 0.0.1
    ---------------------------------------------------------------------------------------

    Last update: 12 / 7 / 2017

    ** Made using pygame, a graphics library and framework for python to give
    game-development tools to anyone who is between new to moderately skilled at coding
    in python

    www.pygame.org
'''

import pygame
from utils import *
from Actors import *

ENABLED = True
PAUSED = False
turnLeft = False
turnRight = False
FRAMERATE = 200
fillColor = Color(255, 0, 0)
width = 800
height = 800
size = (width, height)
display = pygame.display.set_mode(size)

player = Car(True, 554, 120)
CPU = Car(False, 554, 230)
player.setSpeed(4)
CPU.setSpeed(5)

pygame.init()

display = pygame.display.set_mode(size)
pygame.display.set_caption("Pencil E-Racers")
background = image("first map.jpg", [0,0])
clock = pygame.time.Clock()



def drawBackground():
    display.blit(background.image, background.rect)

def showCars():
    player.show(display)
    CPU.show(display)

def updateCars():
    player.update()
    CPU.randomUpdate()

def moveCars():
    player.move()
    CPU.move()

def eventHandler():
    global ENABLED
    global PAUSED
    global turnLeft
    global turnRight
    # event checker
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            ENABLED = False
        elif not PAUSED and event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            turnLeft = True
        elif not PAUSED and event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            turnRight = True
        elif not PAUSED and event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            turnLeft = False
        elif not PAUSED and event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            turnRight = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            PAUSED = not PAUSED
    # Passive action
        # For turning
    if not PAUSED and turnLeft:
        player.setAngle(player.getAngle() - .1)
    if not PAUSED and turnRight:
        player.setAngle(player.getAngle() + .1)
        
# Inhibits a Car's movement if it drives into (collides with) a region outside
# the track.
def canProceed(car):
    global height
    global width
    if car.getY() <= 84 + car.getRadius():
        car.setYSpeed(1)
    if car.getY() >= 701 - car.getRadius():
        car.setYSpeed(-1)
    if car.getX() <= 78 + car.getRadius():
        car.setXSpeed(1)
    if car.getX() >= 730 - car.getRadius():
        car.setXSpeed(-1)
    r = car.getRadius()
    x = car.getX()
    y = car.getY()
    '''if x >= 221 - r and y >= 269 - r and y <= 535 + r:
        if x <= 571 + r:
            car.setXSpeed(-1)
    elif x <= 571 + r and y >= 269 - r and y <= 535 + r:
        if x >= 221 - r:
            car.setXSpeed(1)
    if y >= 269 - r and x >= 221 - r and x <= 571 + r:
        if y <= 535 + r:
            car.setYSpeed(-1)
    elif y <= 535 + r and x >= 221 - r and x <= 571 + r:
        if y >= 269 - r:
            car.setYSpeed(1)'''
    if (x >= 221 - r and x <= 571 + r):
        if (y >= 269 - r and y <= 535 + r):
            if (y > height / 2):
                car.setYSpeed(1)
            else:
                car.setYSpeed(-1)
        if (y >= 269 - r and y <= 535 + r):
            if (x >= 221 - r and x <= 571 + r):
                if (x > width / 2):
                    car.setXSpeed(1)
                else:
                    car.setXSpeed(-1)
                    
#MAIN GAME LOOP
while ENABLED:
    drawBackground()
    showCars()
    pygame.display.update()
    eventHandler()
    if not PAUSED:
        print("dX: ", player.xSpeed, "  dY: ", player.ySpeed, "  X: ", player.x, "  Y:  ", player.y)
        updateCars()
        canProceed(player)
        canProceed(CPU)
        moveCars()
    clock.tick(FRAMERATE)
pygame.quit()
quit()
    
