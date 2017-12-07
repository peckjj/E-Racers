import pygame
from utils import *

class Track1(object):

    def __init__(self, display, color, width, height):
        self.display = display
        self.color = color
        self.width = width
        self.height = height
        
    def show(self):
        ERacers.rect(width / 2, height / 2, width, height, color.getDarker())
        ERacers.rect(width / 2, height / 2, width / 2, height / 2, color.getDarker())
