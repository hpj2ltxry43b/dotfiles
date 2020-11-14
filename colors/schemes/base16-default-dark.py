from utils import *
# adapted from https://raw.githubusercontent.com/aaron-williamson/base16-alacritty/master/colors/base16-default-dark.yml

background = '#181818'
foreground = '#d8d8d8'

black   = '#181818'
red     = '#ab4642'
green   = '#a1b56c'
yellow  = '#f7ca88'
blue    = '#7cafc2'
magenta = '#ba8baf'
cyan    = '#86c1b9'
white   = '#d8d8d8'

bblack   = '#585858'
bred     = '#dc9656'
bgreen   = '#282828'
byellow  = '#383838'
bblue    = '#b8b8b8'
bmagenta = '#e8e8e8'
bcyan    = '#a16946'
bwhite   = '#f8f8f8'

vimColo = 'base16-default-dark'
lockColor = background

alacrittyColors = f'''
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

i3Colors = f'''
set $bg-color            {background}
set $inactive-bg-color   {background}
set $text-color          {foreground}
set $inactive-text-color {darkenHex(foreground, 50)}
set $urgent-bg-color     {darkenHex(red, 50)}
set $moderate-text-color {darkenHex(foreground, 25)}
'''

gtk2Theme = 'Adwaita-dark'
gtk3Theme = 'Adwaita-dark'

gtk2IconTheme = 'Adwaita-Dark'
gtk3IconTheme = 'Adwaita-Dark'
