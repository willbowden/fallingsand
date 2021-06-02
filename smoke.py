from constants import *
from element import Element
import random

class Smoke(Element):

    def __init__(self, x, y, batch):
        self.colors = [(100, 100, 100), (75, 75, 75), (50, 50, 50)]
        self.type = "smoke"
        super().__init__(self.type, x, y, batch)
        self.square.color = random.choice(self.colors)

    def update(self, sim):
        num = random.randint(1, 300)
        if num == 50:
            sim.destroyElement(self)
        else:

            self.square.color = random.choice(self.colors)
            x = self.square.x
            y = self.square.y
        
            if not sim.spaceOccupied(x, y+PS):
                sim.moveElement(self, x, y, x, y+PS)
            elif not sim.spaceOccupied(x-PS, y+PS):
                sim.moveElement(self, x, y, x-PS, y+PS)
            elif not sim.spaceOccupied(x+PS, y+PS):
                sim.moveElement(self, x, y, x+PS, y+PS)
            elif not sim.spaceOccupied(x+PS, y):
                sim.moveElement(self, x, y, x+PS, y)
            elif not sim.spaceOccupied(x-PS, y):
                sim.moveElement(self, x, y, x-PS, y)
            else:
                if sim.getElementType(x, y+PS) in LIQUIDS:
                    sim.swapElements(x, y, x, y+PS)
                elif sim.getElementType(x-PS, y+PS) in LIQUIDS:
                    sim.swapElements(x, y, x-PS, y+PS)
                elif sim.getElementType(x+PS, y+PS) in LIQUIDS:
                    sim.swapElements(x, y, x+PS, y+PS)