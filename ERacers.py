import pygame
from utils import *
from Actors import *

ENABLED = True
PAUSED = False
turnLeft = False
turnRight = False
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
    global turnLeft
    global turnRight
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            ENABLED = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            turnLeft = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            turnRight = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            turnLeft = False
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            turnRight = False
    # Passive action
    if turnLeft:
        player.setAngle(player.getAngle() - .1)
    if turnRight:
        player.setAngle(player.getAngle() + .1)
            
            

# Draws a rectangle from center
def rect(x, y, width, height, color):
    pygame.draw.rect(display, color.getColor(), [x - (width / 2), y - (height / 2), width, height])
    
#MAIN GAME LOOP
while ENABLED:
    print("dX: ", player.xSpeed, "  dY: ", player.ySpeed, "  X: ", player.x, "  Y:  ", player.y)
    drawBackground()
    showCars()
    pygame.display.update()
    eventHandler()
    updateCars()
    clock.tick(60)
pygame.quit()
quit()
    
