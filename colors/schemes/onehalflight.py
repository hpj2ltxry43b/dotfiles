from utils import *

background = '#fafafa'
foreground = '#383a42'

black = '#383a42'
red = '#e45649'
green = '#50a14f'
yellow = '#c18401'
blue = '#0184bc'
magenta = '#a626a4'
cyan = '#0997b3'
white = '#fafafa'

bblack = '#383a42'
bred = '#e45649'
bgreen = '#50a14f'
byellow = '#c18401'
bblue = '#0184bc'
bmagenta = '#a626a4'
bcyan = '#0997b3'
bwhite = '#fafafa'

vimColo = 'onehalflight'
lockColor = background

alacrittyColors = f'''# Colors (One Half Light)
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

dunstLow = (background, lightenHex(foreground, 50))
dunstNormal = (background, foreground)
dunstCritical = (lightenHex(red, 50), foreground)

i3Colors = f'''
set $bg-color            {background}
set $inactive-bg-color   {background}
set $text-color          {foreground}
set $inactive-text-color {lightenHex(foreground, 50)}
set $urgent-bg-color     {lightenHex(red, 50)}
set $moderate-text-color {lightenHex(foreground, 25)}
'''

gtk2Theme = 'Adwaita'
gtk3Theme = 'Adwaita'

gtk2IconTheme = 'Adwaita'
gtk3IconTheme = 'Adwaita'
