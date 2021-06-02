from constants import *
from element import Element
import random

class Bomb(Element):

    def __init__(self, x, y, batch):
        self.colors = [(255,0,0), (10, 10, 10)]
        self.type = "sand"
        super().__init__(self.type, x, y, batch)
        self.square.color = random.choice(self.colors)

    def update(self, sim):
        x = self.square.x
        y = self.square.y

        if y <= UIBARHEIGHT + PS:
            self.explode(sim)
    
        if not sim.spaceOccupied(x, y-PS):
            sim.moveElement(self, x, y, x, y-PS)
        else:
            if sim.getElementType(x, y-PS) not in GASES and sim.getElementType(x, y) != "bomb":
                self.explode(sim)

        
    def explode(self, sim):
        size = 8
        x = int(self.square.x - (size*PS)/2)
        y = int(self.square.y - (size*PS)/2)
        for y2 in range(size):
            for x2 in range(size):
                tempX = x+(x2*PS)
                tempY = y+(y2*PS)
                if tempX >= 0 and tempX <= SPACEWIDTH and tempY >= 0 and tempY <= SCREENHEIGHT:
                    if sim.spaceOccupied(tempX, tempY) and sim.getElementType(tempX, tempY) == "bomb":
                        continue
                    else:
                        sim.destroyElement(None, tempX, tempY)
                        sim.createElement("fire", tempX, tempY)
        sim.destroyElement(self)
