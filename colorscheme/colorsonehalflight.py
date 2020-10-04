import utils

black = (56, 58, 66)
red = (228, 86, 73)
green = (80, 161, 79)
yellow = (193, 132, 1)
blue = (1, 132, 188)
magenta = (166, 38, 164)
cyan = (9, 151, 179)
white = (250, 250, 250)

bblack = (56, 58, 66)
bred = (228, 86, 73)
bgreen = (80, 161, 79)
byellow = (193, 132, 1)
bblue = (1, 132, 188)
bmagenta = (166, 38, 164)
bcyan = (9, 151, 179)
bwhite = (250, 250, 250)

bg = (250, 250, 250)
bgless = bg
bgmore = utils.lighten(*red, 50)

fg = (56, 58, 66)
fgless = utils.lighten(*fg, 50)
fgmore = fg

colors = utils.integerizeColors({
    'black': black,
    'red': red,
    'green': green,
    'yellow': yellow,
    'blue': blue,
    'magenta': magenta,
    'cyan': cyan,
    'white': white,

    'bblack': bblack,
    'bred': bred,
    'bgreen': bgreen,
    'byellow': byellow,
    'bblue': bblue,
    'bmagenta': bmagenta,
    'bcyan': bcyan,
    'bwhite': bwhite,

    'bg': bg,
    'bgless': bgless,
    'bgmore': bgmore,

    'fg': fg,
    'fgless': fgless,
    'fgmore': fgmore,

    'vimcolor': 'onehalflight',
})
