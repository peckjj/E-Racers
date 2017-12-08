import pygame
from utils import *
import math

class Car(pygame.sprite.Sprite):
    IMAGE = image("Car.png", [0,0])
    LEFT = 1
    RIGHT = 2
    
    def __init__ (self, isPlayer, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.isPlayer = isPlayer
        self.angle = math.pi
        self.xSpeed = math.cos(self.angle)
        self.ySpeed = math.sin(self.angle)
        self.x = x
        self.y = y
        self.image = pygame.image.load("Car.png")
        self.radius = 15

    def update(self):
        self.xSpeed = math.cos(self.angle)
        self.ySpeed = math.sin(self.angle)
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def getSpeed(self):
        return self.speed
    
    def getAngle(self):
        return self.angle
    
    def getPosition(self):
        return self.position

    def getImage(self):
        return self.image

    def getRadius(self):
        return self.radius
    
    def isPlayer(self):
        return self.isPlayer
    
    def setSpeed(self, speed):
        self.speed = speed
        
    def setAngle(self, angle):
        self.angle = angle
        
    def setPosition(self, **pos):
        self.position = pos

    def show(self, display):
        pygame.draw.circle(display, (255,0,0), [math.floor(self.x), math.floor(self.y)], self.radius, 0)

