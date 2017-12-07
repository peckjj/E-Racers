import math

class color(object):
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    ORANGE = (255,160,122)
    YELLOW = (255,255,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    PURPLE = (128,0,128)
    
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def getColor(self):
        print([self.r, self.g, self.b])
        return (self.r,self.g,self.b)

    def getBrighter(self):
        return (max(255, self.r + 50), max(255, self.g + 50), max(255, self.b + 50))

    def getDarker(self):
        return (max(255, self.r - 50), max(255, self.g - 50), max(255, self.b - 50))
    
        
