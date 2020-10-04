import utils

black = (40, 44, 52)
red = (224, 108, 117)
green = (152, 195, 121)
yellow = (229, 192, 123)
blue = (97, 175, 239)
magenta = (198, 120, 221)
cyan = (86, 182, 194)
white = (220, 223, 228)

bblack = (40, 44, 52)
bred = (224, 108, 117)
bgreen = (152, 195, 121)
byellow = (229, 192, 123)
bblue = (97, 175, 239)
bmagenta = (198, 120, 221)
bcyan = (86, 182, 194)
bwhite = (220, 223, 228)

bg = (40, 44, 52)
bgless = bg
bgmore = utils.darken(*red, 50)

fg = (220, 223, 228)
fgless = utils.darken(*fg, 50)
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

    'vimcolor': 'onehalfdark',
})
