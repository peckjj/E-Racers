import pygame
from utils import *

class Track1:

    def __init__(self, display, color, width, height):
        self.display = display
        self.color = color
        self.width = width
        self.height = height
        
    def show(self):
        pygame.draw.rect(self.display, self.color.getDarker(), [0, 0, self.width, self.height])
        pygame.draw.rect(self.display, self.color.getDarker(), [self.width / 4, self.width / 4, self.width / 2, self.width / 2])
