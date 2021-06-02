PS = 10
SPACEHEIGHT = 600
SPACEWIDTH = 800
UIBARHEIGHT = 200
UIBARWIDTH = SPACEWIDTH
SCREENHEIGHT = UIBARHEIGHT + SPACEHEIGHT
SCREENWIDTH = SPACEWIDTH
MAXBRUSHSIZE = 8

UILAYOUT = [["sand", "water", "fire", "wood"], ["stone", "lava", "bomb", "rSand"], ["glass", "acid"]]

FONT = "Arial"
UIITEMCOUNT = 0
for item in UILAYOUT:
    for thing in item:
        UIITEMCOUNT += 1

FONTSIZE = 160 * (1 / UIITEMCOUNT)

LIQUIDS = ["water", "lava"]
GASES = ["smoke", "fire"]
FLAMMABLES = ["wood"]
ACIDPROOF = ["glass", "acid"]

RAINBOW = [(255,0,0), (255,140,0), (255,255,0), (0,255,0), (0,0,255), (255,0,255), (128,0,128)]