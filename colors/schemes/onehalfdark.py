from utils import *

background = '#282c34'
foreground = '#dcdfe4'

black = '#282c34'
red = '#e06c75'
green = '#98c379'
yellow = '#e5c07b'
blue = '#61afef'
magenta = '#c678dd'
cyan = '#56b6c2'
white = '#dcdfe4'

bblack = '#282c34'
bred = '#e06c75'
bgreen = '#98c379'
byellow = '#e5c07b'
bblue = '#61afef'
bmagenta = '#c678dd'
bcyan = '#56b6c2'
bwhite = '#dcdfe4'

vimColo = 'onehalfdark'
lockColor = background

alacrittyColors = f'''# Colors (One Half Dark)
colors:
  primary:
    background: '{background}'
    foreground: '{foreground}'

  normal:
    black: '{black}'
    red: '{red}'
    green: '{green}'
    yellow: '{yellow}'
    blue: '{blue}'
    magenta: '{magenta}'
    cyan: '{cyan}'
    white: '{white}'

  bright:
    black: '{bblack}'
    red: '{bred}'
    green: '{bgreen}'
    yellow: '{byellow}'
    blue: '{bblue}'
    magenta: '{bmagenta}'
    cyan: '{bcyan}'
    white: '{bwhite}'
'''

dunstLow = (background, darkenHex(foreground, 50))
dunstNormal = (background, foreground)
dunstCritical = (darkenHex(red, 50), foreground)
