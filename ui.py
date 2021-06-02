from constants import *
from element_selector import elementSelector as eS
from element_types import *

class ui:
    def __init__(self, batch):
        self.width = UIBARWIDTH
        self.height = UIBARHEIGHT
        self.batch = batch
        self.objects = []
        self.activatedSelection = None
        numOfRows = len(UILAYOUT)
        for i in range(numOfRows):
            numOfLabels = len(UILAYOUT[i])
            for j in range(numOfLabels):
                paddingX = (UIBARWIDTH/numOfLabels) / 2
                y = int( 30 + (i * (UIBARHEIGHT/numOfRows)))
                x = int(paddingX + (j * (UIBARWIDTH/numOfLabels)))
                temp = eS(UILAYOUT[i][j], UILAYOUT[i][j].capitalize(), x, y, self.batch)
                temp.boxWidth = (j+1 * (UIBARWIDTH/numOfLabels))
                temp.boxHeight = (i+1 * (UIBARHEIGHT/numOfRows))
                temp.calcArea()
                self.objects.append(temp)



    def uiClicked(self, x, y):
        for thing in self.objects:
            if thing.withinBounds(x, y):
                if not thing.activated:
                    if self.activatedSelection != None:
                        self.activatedSelection.activated = False
                        self.activatedSelection.updateColor()
                    thing.activated = True
                    self.activatedSelection = thing
                else:
                    thing.activated = False
                    self.activatedSelection = None
            thing.updateColor()
        if self.activatedSelection != None:
            return self.activatedSelection.elementType
        else:
            return None        