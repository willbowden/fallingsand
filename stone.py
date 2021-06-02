from constants import *
from element import Element
import random

class Stone(Element):

    def __init__(self, x, y, batch):
        self.colors = [(95, 95, 95)]
        self.type = "stone"
        super().__init__(self.type, x, y, batch)
        self.square.color = random.choice(self.colors)

    def update(self, sim):
        return