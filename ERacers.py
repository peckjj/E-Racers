import pygame
from utils import *

pygame.init()

display = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pencil E-Racers")

ENABLED = True

display.fill(color.PURPLE)

def update():
    pygame.display.update()

while ENABLED:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ENABLED = False
    update()

pygame.quit()
quit()
        
