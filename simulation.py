import pyglet as pg
from pyglet import clock
from constants import *
from element import Element
from element_types import *
from helpers import *
from ui import ui
import random

class Simulation:
    def __init__(self):
        self.window = pg.window.Window(width=SCREENWIDTH, height=SCREENHEIGHT)
        self.batch = pg.graphics.Batch()
        self.elements = []
        self.space = []
        self.ui = ui(self.batch)
        self.selectedElement = "sand"
        self.brushSize = 4
        self.brushSizeLabel = None
        self.timer = 0
        for y in range(SCREENHEIGHT+1):
            self.space.append([])
            for x in range(SCREENWIDTH+1):
                self.space[y].append(None)

    def createElement(self, elType, x, y):
        if withinSpaceBounds(x, y):
            if not self.spaceOccupied(x, y):
                temp = ELEMENT_TYPES[elType](x, y, self.batch)
                self.elements.append(temp)
                self.space[y][x] = temp

    def updateSpace(self, dt):
        if self.timer >= 1.5:
            self.brushSizeLabel = None
            self.timer = 0
        else:
            self.timer += dt
        for element in self.elements:
            x = element.square.x
            y = element.square.y
            if y >= UIBARHEIGHT and y <= SCREENHEIGHT - PS:
                if x >= 0 and x <= SCREENWIDTH - PS:
                    element.update(self)

    def getElementType(self, x, y):
        return self.space[y][x].type

    def spaceOccupied(self, x, y):
        if self.space[y][x] != None:
            return True
        else:
            return False
    
    def swapElements(self, x1, y1, x2, y2):
        if self.space[y1][x1] != None and self.space[y2][x2] != None:
            temp = self.space[y1][x1]
            self.space[y1][x1] = self.space[y2][x2]
            self.space[y1][x1].square.x = x1
            self.space[y1][x1].square.y = y1
            self.space[y2][x2] = temp
            self.space[y2][x2].square.x = x2
            self.space[y2][x2].square.y = y2

    def surroundingElements(self, x, y):
        s = self.space
        n = PS
        return [s[y+n][x-n], s[y+n][x], s[y+n][x+n],
         s[y][x-n], s[y][x], s[y][x+n],
          s[y-n][x-n], s[y-n][x], s[y-n][x+n]]

    def immediateSurroundings(self, x, y):
        s = self.space
        n = PS
        return [s[y+n][x], s[y][x+n],
         s[y][x-n], s[y-n][x]]

    def moveElement(self, element, oldX, oldY, newX, newY):
        if newY >= UIBARHEIGHT:
            element.square.color = random.choice(element.colors)
            self.space[oldY][oldX] = None
            self.space[newY][newX] = element
            element.square.x = newX
            element.square.y = newY

    def destroyElement(self, element=None, x=None, y=None):
        if element != None:
            x = element.square.x
            y = element.square.y
            if element in self.elements:
                self.elements.remove(element)
        else:
            element = self.space[y][x]
            if element in self.elements:
                self.elements.remove(element)
        self.space[y][x] = None


    def clearSpace(self):
        self.elements = []
        self.space = []
        for y in range(SCREENHEIGHT+1):
            self.space.append([])
            for x in range(SCREENWIDTH+1):
                self.space[y].append(None)

    def changeBrushSize(self, size, x, y):
        self.brushSize = int(size)
        self.brushSizeLabel = pg.text.Label(str(int(self.brushSize)), FONT, 16, x=x, y=y+20, color=(255, 0, 0, 255))

    def runSimulation(self):
        divider = pg.shapes.Rectangle(x=0, y=UIBARHEIGHT-3, width=SCREENWIDTH, height=3, color=(200, 200, 200))
        @self.window.event
        def on_draw():
            self.window.clear()
            divider.draw()
            self.batch.draw()
            if self.brushSizeLabel != None:
                self.brushSizeLabel.draw()

        @self.window.event
        def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
            n = self.brushSize #Brush size
            x = myRound(x)
            y = myRound(y)
            if x >= 0 and x <= (SCREENWIDTH - PS):
                if y >= UIBARHEIGHT and y <= (SCREENHEIGHT - PS):
                    if buttons & pg.window.mouse.LEFT:
                        if self.selectedElement != None:
                            for a in range(n):
                                for b in range(n):
                                    self.createElement(self.selectedElement, x+a*PS, y+b*PS)
                    if buttons & pg.window.mouse.RIGHT:
                        for a in range(n):
                            for b in range(n):
                                self.destroyElement(None, x+a*PS, y+b*PS)
        @self.window.event
        def on_key_press(symbol, modifiers):
            if symbol == pg.window.key.R:
                self.clearSpace()
            if symbol == pg.window.key.UP:
                if (self.brushSize + 1) > MAXBRUSHSIZE:
                    self.changeBrushSize(MAXBRUSHSIZE, SCREENWIDTH/2, UIBARHEIGHT/2)
                else:
                    self.changeBrushSize(self.brushSize + 1, SCREENWIDTH/2, UIBARHEIGHT/2)
            if symbol == pg.window.key.DOWN:
                if (self.brushSize - 1) < 1:
                    self.changeBrushSize(1, SCREENWIDTH/2, UIBARHEIGHT/2)
                else:
                    self.changeBrushSize(self.brushSize - 1, SCREENWIDTH/2, UIBARHEIGHT/2)

        @self.window.event
        def on_mouse_scroll(x, y, scroll_x, scroll_y):
            if (self.brushSize + scroll_y) > MAXBRUSHSIZE:
                self.changeBrushSize(MAXBRUSHSIZE, x, y)
            elif (self.brushSize + scroll_y) < 1:
                self.changeBrushSize(1, x, y)
            else:
                self.changeBrushSize(self.brushSize + scroll_y, x, y)
                

        @self.window.event
        def on_mouse_press(x, y, button, modifiers):
            n = self.brushSize #Brush size
            x = myRound(x)
            y = myRound(y)
            if x >= 0 and x <= UIBARWIDTH and y >= 0 and y < UIBARHEIGHT:
                self.selectedElement = self.ui.uiClicked(x, y)
            if x >= 0 and x <= (SCREENWIDTH - (n * PS)):
                if y >= UIBARHEIGHT and y <= (SCREENHEIGHT - PS):
                    if button == pg.window.mouse.LEFT:
                        if self.selectedElement != None:
                            for a in range(n):
                                for b in range(n):
                                    self.createElement(self.selectedElement, x+a*PS, y+b*PS)
                    elif button == pg.window.mouse.RIGHT:
                        for a in range(n):
                            for b in range(n):
                                self.destroyElement(None, x+a*PS, y+b*PS)

        clock.schedule(self.updateSpace)
        pg.app.run()

        while True:
            clock.tick()