from constants import *

def withinSpaceBounds(x, y):
    if x >= 0 and x <= SPACEWIDTH:
        if y <= SCREENHEIGHT and y >= UIBARHEIGHT:
            return True
        else:
            return False
    else:
        return False

def myRound(x, base=PS):
    return int(base * round(float(x)/base))

def rainbowGradient(color, step=5):
    red, green, blue = color

    if red == 255 and green == 255 and blue == 255:
        green = 0
        blue = 0
    if red < 255 and green == 0 and blue == 0:
        red += step
    if red == 255 and green < 255 and blue == 0:
        green += step
    if red > 0 and green == 255 and blue == 0:
        red -= step
    if red == 0 and green == 255 and blue < 255:
        blue += step
    if red == 0 and green > 0 and blue == 255:
        green -= step
    if red < 255 and green == 0 and blue == 255:
        red += step
    if red == 255 and green == 0 and blue > 0:
        blue -= step

    return ( red, green, blue )