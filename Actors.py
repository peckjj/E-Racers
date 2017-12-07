import pygame
from utils import *

class Car(object):
    def __init__ (self, isPlayer):
        self.isPlayer = isPlayer
        self.angle = 0;
        self.speed = 0;
        self.position = [0,0]

    def update(self):
        print()

    def getSpeed(self):
        return self.speed
    
    def getAngle(self):
        return self.angle
    
    def getPosition(self):
        return self.position
    
    def isPlayer(self):
        return self.isPlayer
    
    def setSpeed(self, speed):
        self.speed = speed
        
    def setAngle(self, angle):
        self.angle = angle
        
    def setPosition(self, **pos):
        self.position = pos

