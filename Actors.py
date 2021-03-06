import pygame
from utils import *
import math
import random

class Car(pygame.sprite.Sprite):
    IMAGE = image("Car.png", [0,0])
    LEFT = 1
    RIGHT = 2
    pink = (255,105,180)
    
    def __init__ (self, isPlayer, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.isPlayer = isPlayer
        self.angle = math.pi
        self.speed = 1
        self.xSpeed = self.speed * math.cos(self.angle)
        self.ySpeed = self.speed * math.sin(self.angle)
        self.x = x
        self.y = y
        self.image = pygame.image.load("Car.png")
        self.radius = 15
        self.lap = 0
        self.passCheck = True

    def update(self):
        self.xSpeed = self.speed * math.cos(self.angle)
        self.ySpeed = self.speed * math.sin(self.angle)

    def randomUpdate(self):
        rand = random.random()
        if rand < .002:
            self.angle = self.angle + 1
        elif rand < .033 and self.lap != 0:
            self.angle = self.angle - 1
        self.update()

    def move(self):
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def stop(self):
        self.xSpeed = 0
        self.ySpeed = 0

    def getSpeed(self):
        return self.speed

    def getXSpeed(self):
        return self.xSpeed

    def getYSpeed(self):
        return self.ySpeed
    
    def getAngle(self):
        return self.angle

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def getPosition(self):
        return self.position

    def getImage(self):
        return self.image

    def getRadius(self):
        return self.radius

    def getLap(self):
        return self.lap
    
    def isPlayer(self):
        return self.isPlayer

    def setSpeed(self, speed):
        self.speed = speed
    
    def setXSpeed(self, speed):
        self.xSpeed = speed

    def setYSpeed(self, speed):
        self.ySpeed = speed
        
    def setAngle(self, angle):
        self.angle = angle
        
    def setPosition(self, **pos):
        self.position = pos

    def addLap(self):
        self.lap = self.lap + 1
        print(self.lap)

    def subtractLap(self):
        self.lap = self.lap - 1
        print(self.lap)

    def show(self, display):
        pygame.draw.circle(display, Car.pink, [int(self.x), int(self.y)], self.radius, 0)

