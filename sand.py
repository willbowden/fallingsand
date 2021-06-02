from constants import *
from element import Element
import random

class Sand(Element):

    def __init__(self, x, y, batch):
        self.colors = [(255, 225, 0), (190, 175, 0), (255, 240, 95)]
        self.type = "sand"
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
        else:
            if sim.getElementType(x, y-PS) in LIQUIDS and sim.getElementType(x, y-PS) != "lava":
                sim.swapElements(x, y, x, y-PS)
            elif sim.getElementType(x-PS, y-PS) in LIQUIDS and sim.getElementType(x-PS, y-PS) != "lava":
                sim.swapElements(x, y, x-PS, y-PS)
            elif sim.getElementType(x+PS, y-PS) in LIQUIDS and sim.getElementType(x+PS, y-PS) != "lava":
                sim.swapElements(x, y, x+PS, y-PS)
