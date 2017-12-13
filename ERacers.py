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

pygame.init()
pygame.font.init()


ENABLED = True
GAME_OVER = False
PAUSED = False
turnLeft = False
turnRight = False
initPlayerStart = (554, 120)
initCPUStart = (554, 230)
FRAMERATE = 60
turnSpeed = .1
PLAYER_SPEED = 40
passCheck = True
passCheck2 = True
CPU_SPEED = PLAYER_SPEED * 1.2
collisionSetback = 2
winner = ""
fillColor = Color(255, 0, 0)
width = 800
height = 800
size = (width, height)
display = pygame.display.set_mode(size)
font = pygame.font.SysFont("Times New Roman", 40)
text = None

player = Car(True, initPlayerStart[0], initPlayerStart[1])
CPU = Car(False, initCPUStart[0], initCPUStart[1])
player.setSpeed(PLAYER_SPEED)
CPU.setSpeed(CPU_SPEED)


display = pygame.display.set_mode(size)
pygame.display.set_caption("Pencil E-Racers")
background = image("first map.jpg", [0,0])
clock = pygame.time.Clock()

def init():
    global ENABLED, PAUSED, turnLeft, turnRight, initPlayerStart, initCPUStart
    global FRAMERATE, turnSpeed, PLAYER_SPEED, passCheck, passCheck2
    global CPU_SPEED, collisionSetback, fillColor, width, height, size, display
    global player, CPU, winner, font, text, GAME_OVER
    ENABLED = True
    GAME_OVER = False
    PAUSED = False
    turnLeft = False
    turnRight = False
    initPlayerStart = (554, 120)
    initCPUStart = (554, 230)
    FRAMERATE = 60
    turnSpeed = .2
    PLAYER_SPEED = 10
    passCheck = True
    passCheck2 = True
    CPU_SPEED = PLAYER_SPEED * 1.3
    collisionSetback = 2.3
    winner = ""
    fillColor = Color(255, 0, 0)
    width = 800
    height = 800
    size = (width, height)
    display = pygame.display.set_mode(size)
    font = pygame.font.SysFont("Times New Roman", 40)
    text = None

    player = Car(True, initPlayerStart[0], initPlayerStart[1])
    CPU = Car(False, initCPUStart[0], initCPUStart[1])
    player.setSpeed(PLAYER_SPEED)
    CPU.setSpeed(CPU_SPEED)

    pygame.init()

    display = pygame.display.set_mode(size)
    pygame.display.set_caption("Pencil E-Racers")
    background = image("first map.jpg", [0,0])
    clock = pygame.time.Clock()

def drawBackground():
    global text
    if player.getLap() <= 1:
        laps = "Lap: 1"
    elif player.getLap() >= 3:
        laps = "Lap: 3"
    else:
        laps = "Lap: " + str(player.getLap())
    display.blit(background.image, background.rect)
    text = font.render(laps, True, Color.BLACK)
    display.blit(text, (width - 200, 20))

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
    global turnSpeed, GAME_OVER
    # event checker
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            ENABLED = False
            GAME_OVER = False
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
        # Restart Checker
        if event.type == pygame.MOUSEBUTTONDOWN and GAME_OVER:
            x = event.pos[0]
            y = event.pos[1]
            inYes = (x > 335 and x < 386) and (y > 446 and y < 495)
            inNo = (x > 405 and x < 456) and (y > 446 and y < 495)
            if inYes:
                init()
                GAME_OVER = False
                ENABLED = True
            if inNo:
                pygame.quit()
                quit()
    # Passive action
        # For turning
    if not PAUSED and turnLeft:
        player.setAngle(player.getAngle() - turnSpeed)
    if not PAUSED and turnRight:
        player.setAngle(player.getAngle() + turnSpeed)


def lapManager(car, inside):
    if inside and car.passCheck:
        if (car.getXSpeed() < 0):
            car.addLap()
        if (car.getXSpeed() > 0):
            car.subtractLap()
        car.passCheck = False
    if not inside:
        car.passCheck = True
        
    
init()
# Inhibits a Car's movement if it drives into (collides with) a region outside
# the track.
def collisionCheck(car):
    global height
    global width
    global collisionSetback
    global passCheck
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
    inY = (y <= 269 - r)
    inX = (x >= 445 - r and x <= 512 + r)
    # Finish line collision handler
    lapManager(car, inY and inX)
    

def checkWinner():
    global GAME_OVER, winner
    if player.getLap() == 4:
        GAME_OVER = True
        winner = "Player"
    elif CPU.getLap() == 4:
        GAME_OVER = True
        winner = "CPU"
        
                    
#MAIN GAME LOOP
while ENABLED:
    drawBackground()
    showCars()
    pygame.display.update()
    eventHandler()
    if not PAUSED:
       # print("dX: ", player.xSpeed, "  dY: ", player.ySpeed, "  X: ", player.x, "  Y:  ", player.y)
        updateCars()
        collisionCheck(player)
        collisionCheck(CPU)
        moveCars()
        checkWinner()
    while GAME_OVER:
        drawBackground()
        showCars()
        eventHandler()
        pygame.draw.rect(display, Color.YELLOW, (width / 2 - 200, height / 2 - 100, 400, 200), 0)
        pygame.draw.rect(display, Color.GREEN, (width / 2 - 35 - 30, height / 2 + 45, 50, 50), 0)
        pygame.draw.rect(display, Color.RED, (width / 2 + 35 - 30, height / 2 + 45, 50, 50), 0)
        winMessage = winner + " Wins!"
        text = font.render(winMessage, True, (0,0,0))
        display.blit(text, (width / 2 - 100, height / 2 - 95))
        text = font.render("Play Again?", True, (0,0,0))
        display.blit(text, (width / 2 - 100, height / 2 - 55))
        text = font.render("Y", True, (255,255,255))
        display.blit(text, (width / 2 - 35 - 20, height / 2 + 45))
        text = font.render("N", True, (255,255,255))
        display.blit(text, (width / 2 + 35 - 20, height / 2 + 45))
        pygame.display.update()
        
        
    clock.tick(FRAMERATE)
pygame.quit()
quit()
    
