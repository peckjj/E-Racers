import pygame
from utils import *
from Actors import *

ENABLED = True
fillColor = Color(255, 0, 0)
width = 800
height = 600
display = pygame.display.set_mode((width, height))
size = (800,800)

player = Car(True)
CPU = Car(False)

pygame.init()

display = pygame.display.set_mode(size)
pygame.display.set_caption("Pencil E-Racers")
background = image("first map.jpg", [0,0])



def update():
    display.blit(background.image, background.rect)
    pygame.display.update()

# Draws a rectangle from center
def rect(x, y, width, height, color):
    pygame.draw.rect(display, color.getColor(), [x - (width / 2), y - (height / 2), width, height])
    

while ENABLED:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ENABLED = False
    update()

pygame.quit()
quit()
    
