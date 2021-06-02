from constants import *
from element import Element
import random

class Lava(Element):

    def __init__(self, x, y, batch):
        self.colors = [(233,105,44), (255,79,0), (255,69,0)]
        self.type = "lava"
        super().__init__(self.type, x, y, batch)
        self.square.color = random.choice(self.colors)

    def update(self, sim):
        x = self.square.x
        y = self.square.y

        surroundings = sim.surroundingElements(x, y)
        temp = [x for x in surroundings if x != None]
        for item in temp:
            if item.type == "water":
                tempX = item.square.x
                tempY = item.square.y
                sim.destroyElement(item)
                sim.destroyElement(self)
                sim.createElement("stone", x, y)
                sim.createElement("steam", tempX, tempY)
            elif item.type == "sand":
                tempX = item.square.x
                tempY = item.square.y
                sim.destroyElement(item)
                sim.destroyElement(self)
                sim.createElement("glass", tempX, tempY)
        matches = [x for x in temp if x.type in FLAMMABLES]
        if len(matches) != 0:
            for item in matches:
                r = random.randint(1, 50)
                if r == 3:
                    sim.destroyElement(item)
                    sim.createElement("fire", item.square.x, item.square.y)
                    if not sim.spaceOccupied(x, y+1):
                        sim.createElement("smoke", x, y+1)
                    elif not sim.spaceOccupied(x, y-1):
                        sim.createElement("smoke", x, y-1)
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