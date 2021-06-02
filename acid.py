from constants import *
from element import Element
import random

class Acid(Element):

    def __init__(self, x, y, batch):
        self.colors = [(50, 255, 50), (0, 255, 0), (0, 210, 0)]
        self.type = "acid"
        super().__init__(self.type, x, y, batch)
        self.square.color = random.choice(self.colors)

    def update(self, sim):
        x = self.square.x
        y = self.square.y

        surroundings = sim.surroundingElements(x, y)
        temp = [x for x in surroundings if x != None]
        for item in temp:
            if item.type == "water":
                sim.destroyElement(self)
                sim.createElement("water", x, y)
            elif item.type not in ACIDPROOF and item.type != "water":
                r = random.randint(1, 5)
                if r == 1:
                    sim.destroyElement(item)


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