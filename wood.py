from constants import *
from element import Element
import random

class Wood(Element):

    def __init__(self, x, y, batch):
        self.colors = [(72,6,7), (89,39,32), (78,22,9)]
        self.type = "wood"
        super().__init__(self.type, x, y, batch)
        self.square.color = random.choice(self.colors)

    def update(self, sim):
        return