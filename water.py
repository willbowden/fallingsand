from constants import *
from element import Element
import random

class Water(Element):

    def __init__(self, x, y, batch):
        self.colors = [(0, 255, 255)]
        self.type = "water"
        super().__init__(self.type, x, y, batch)
        self.square.color = random.choice(self.colors)

    def update(self, sim):
        x = self.square.x
        y = self.square.y
        
        if not sim.spaceOccupied(x, y-PS):
            sim.moveElement(self, x, y, x, y-PS)
        elif not sim.spaceOccupied(x-PS, y-PS):
            sim.moveElement(self, x, y, x-PS, y-PS)
        elif not sim.spaceOccupied(x+PS, y-PS):
            sim.moveElement(self, x, y, x+PS, y-PS)
        elif not sim.spaceOccupied(x+PS, y):
            sim.moveElement(self, x, y, x+PS, y)
        elif not sim.spaceOccupied(x-PS, y):
            sim.moveElement(self, x, y, x-PS, y)