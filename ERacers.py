import pygame
from utils import *

ENABLED = True
fillColor = Color(255, 0, 0)
width = 800
height = 600
display = pygame.display.set_mode((width, height))
track = Track1(display, fillColor, width, height)

pygame.init()

display = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pencil E-Racers")

display.fill(fillColor.getColor())


def update():
    pygame.display.update()

# Draws a rectangle from center
def rect(x, y, width, height, color):
    pygame.draw.rect(display, color.getColor(), [x - (width / 2), y - (height / 2), width, height])
    

while ENABLED:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ENABLED = False
    track.show()
    update()

pygame.quit()
quit()
    
