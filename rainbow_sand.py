from constants import *
from element import Element
from helpers import *
import random

class RainbowSand(Element):

    def __init__(self, x, y, batch):
        self.colors = RAINBOW
        self.type = "rSand"
        super().__init__(self.type, x, y, batch)

    def update(self, sim):
        self.square.color = rainbowGradient(self.square.color)
        x = self.square.x
        y = self.square.y
        
        if not sim.spaceOccupied(x, y-PS):
            sim.moveElement(self, x, y, x, y-PS)
        elif not sim.spaceOccupied(x-PS, y-PS):
            sim.moveElement(self, x, y, x-PS, y-PS)
        elif not sim.spaceOccupied(x+PS, y-PS):
            sim.moveElement(self, x, y, x+PS, y-PS)
        else:
            if sim.getElementType(x, y-PS) in LIQUIDS:
                sim.swapElements(x, y, x, y-PS)
            elif sim.getElementType(x-PS, y-PS) in LIQUIDS:
                sim.swapElements(x, y, x-PS, y-PS)
            elif sim.getElementType(x+PS, y-PS) in LIQUIDS:
                sim.swapElements(x, y, x+PS, y-PS)