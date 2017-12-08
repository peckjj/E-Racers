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
size = (800, 800)
display = pygame.display.set_mode(size)

player = Car(True, 554, 120)
CPU = Car(False, 554, 230)

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
    CPU.update()

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
            
def canProceed():
    global player
    global CPU
    
    
#MAIN GAME LOOP
while ENABLED:
    drawBackground()
    showCars()
    pygame.display.update()
    eventHandler()
    if not PAUSED:
        print("dX: ", player.xSpeed, "  dY: ", player.ySpeed, "  X: ", player.x, "  Y:  ", player.y)
        updateCars()
    clock.tick(FRAMERATE)
pygame.quit()
quit()
    
