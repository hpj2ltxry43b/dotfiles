import utils

black = (40, 44, 52)
red = (224, 108, 117)
green = (152, 195, 121)
yellow = (229, 192, 123)
blue = (97, 175, 239)
magenta = (198, 120, 221)
cyan = (86, 182, 194)
white = (220, 223, 228)

dblack = utils.darken(*black, 50)
dred = utils.darken(*red, 50)
dgreen = utils.darken(*green, 50)
dyellow = utils.darken(*yellow, 50)
dblue = utils.darken(*blue, 50)
dmagenta = utils.darken(*magenta, 50)
dcyan = utils.darken(*cyan, 50)
dwhite = utils.darken(*white, 50)

bblack = utils.lighten(*black, 50)
bred = utils.lighten(*red, 50)
bgreen = utils.lighten(*green, 50)
byellow = utils.lighten(*yellow, 50)
bblue = utils.lighten(*blue, 50)
bmagenta = utils.lighten(*magenta, 50)
bcyan = utils.lighten(*cyan, 50)
bwhite = utils.lighten(*white, 50)

bg = black
bgless = bg
bgmore = red

fg = white
fgless = dwhite
fgmore = white

colors = utils.integerizeColors({
    "bg": bg,
    "bgless": bgless,
    "bgmore": bgmore,

    "fg": fg,
    "fgless": fgless,
    "fgmore": fgmore,

    "dblack": dblack,
    "dred": dred,
    "dgreen": dgreen,
    "dyellow": dyellow,
    "dblue": dblue,
    "dmagenta": dmagenta,
    "dcyan": dcyan,
    "dwhite": dwhite,

    "black": black,
    "red": red,
    "green": green,
    "yellow": yellow,
    "blue": blue,
    "magenta": magenta,
    "cyan": cyan,
    "white": white,

    "bblack": bblack,
    "bred": bred,
    "bgreen": bgreen,
    "byellow": byellow,
    "bblue": bblue,
    "bmagenta": bmagenta,
    "bcyan": bcyan,
    "bwhite": bwhite,
})
