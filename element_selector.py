from constants import *
import pyglet as pg

class elementSelector:
    def __init__(self, elementType, text, x, y, batch):
        self.elementType = elementType
        self.activated = False
        self.text = pg.text.Label(text, FONT, FONTSIZE, x=x, y=y, anchor_x="center", anchor_y="center", batch=batch)
        self.boxWidth = 0
        self.boxHeight = 0

    def calcArea(self):
        self.right = self.text.x + (self.boxWidth / 2)
        self.left = self.text.x - (self.boxWidth / 2)
        self.top = self.text.y + (self.boxHeight / 2)
        self.bottom = self.text.y - (self.boxHeight / 2)

    def withinBounds(self, x, y):
        if x >= self.left and x <= self.right and y >= self.bottom and y <= self.top:
            return True
        else:
            return False
        
    def updateColor(self):
        if self.activated:
            self.text.color = (0, 255, 255, 255)
        else:
            self.text.color = (255, 255, 255, 255)
