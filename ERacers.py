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
initPlayerStart = (554, 120)
initCPUStart = (554, 230)
FRAMERATE = 100
turnSpeed = .75
collisionSetback = 15
fillColor = Color(255, 0, 0)
width = 800
height = 800
size = (width, height)
display = pygame.display.set_mode(size)

player = Car(True, initPlayerStart[0], initPlayerStart[1])
CPU = Car(False, initCPUStart[0], initCPUStart[1])
player.setSpeed(15)
CPU.setSpeed(8)

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
    global turnSpeed
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
        player.setAngle(player.getAngle() - turnSpeed)
    if not PAUSED and turnRight:
        player.setAngle(player.getAngle() + turnSpeed)
        
# Inhibits a Car's movement if it drives into (collides with) a region outside
# the track.
def canProceed(car):
    global height
    global width
    global collisionSetback
    # Outer bound checker
    if car.getY() <= 84 + car.getRadius():
        car.setYSpeed(collisionSetback)
    if car.getY() >= 701 - car.getRadius():
        car.setYSpeed(-collisionSetback)
    if car.getX() <= 78 + car.getRadius():
        car.setXSpeed(collisionSetback)
    if car.getX() >= 730 - car.getRadius():
        car.setXSpeed(-collisionSetback)
    r = car.getRadius()
    x = car.getX()
    y = car.getY()
    # More complex inner bound checker
    if (x >= 221 - r and x <= 571 + r):
        if (y >= 269 - r and y <= 535 + r):
            if (y > height / 2):
                car.setYSpeed(collisionSetback)
            else:
                car.setYSpeed(-collisionSetback)
        if (y >= 269 - r and y <= 535 + r):
            if (x >= 221 - r and x <= 571 + r):
                if (x > width / 2):
                    car.setXSpeed(collisionSetback)
                else:
                    car.setXSpeed(-collisionSetback)
                    
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
    
