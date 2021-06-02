from constants import *
from element import Element
import random

class Glass(Element):

    def __init__(self, x, y, batch):
        self.colors = [(0, 200, 200)]
        self.type = "glass"
        super().__init__(self.type, x, y, batch)
        self.square.color = random.choice(self.colors)

    def update(self, sim):
        return