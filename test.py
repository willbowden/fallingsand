def rainbowGradient( colour ):
    red, green, blue = colour

    if red < 255 and green == 0 and blue == 0:
        red += 1
    if red == 255 and green < 255 and blue == 0:
        green += 1
    if red > 0 and green == 255 and blue == 0:
        red -= 1
    if red == 0 and green == 255 and blue < 255:
        blue += 1
    if red == 0 and green > 0 and blue == 255:
        green -= 1
    if red < 255 and green == 0 and blue == 255:
        red += 1
    if red == 255 and green == 0 and blue > 0:
        blue -= 1

    return ( red, green, blue )
    