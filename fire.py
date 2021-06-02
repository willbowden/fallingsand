from constants import *
from element import Element
import random

class Fire(Element):

    def __init__(self, x, y, batch):
        self.colors = [(220, 50, 10), (255, 120, 0), (255, 160, 0)]
        self.type = "smoke"
        super().__init__(self.type, x, y, batch)
        self.square.color = random.choice(self.colors)

    def update(self, sim):
        self.square.color = random.choice(self.colors)
        x = self.square.x
        y = self.square.y
    
        surroundings = sim.surroundingElements(x, y)
        temp = [x for x in surroundings if x != None]
        for item in temp:
            if item.type == "water":
                sim.destroyElement(self)
                sim.createElement("steam", x, y)
                break
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
        else:
            r = random.randint(1, 2)
            sim.destroyElement(self)
            if r == 2:
                sim.createElement("smoke", x, y)