from pyglet import shapes
from constants import *

class Element:
    def __init__(self, type, initialX, initialY, batch):
        color = (255, 0, 0)
        self.square = shapes.Rectangle(x=initialX, y=initialY, width=PS, height=PS, color=color, batch=batch)

    def move(self, sim):
        x = self.square.x
        y = self.square.y
        if self.momentum[0] != 0 or self.momentum[1] != 0:
            sim.moveElement(self, x, y, x+(PS*self.momentum[0]), y+(PS*self.momentum[1]))
            self.square.x += (PS*self.momentum[0])
            self.square.y += (PS*self.momentum[1])