import sys
import re
import importlib

def formatColor(name, color):
    colorr, colorg, colorb = color

    fcolor = 30 if colorr + colorg + colorb > 381 else 37

    return f'\033[48;2;{colorr};{colorg};{colorb}m\033[{fcolor}m{name}\033[0m'

def rgbToHex(color):
    return '#' + ''.join(hex(c)[2:].zfill(2) for c in color)

files = [
    '../alacritty/.config/alacritty/alacritty_preset.yml',
    '../i3/.config/i3/config_preset',
    '../bin/bin/lock_preset.sh',
    '../dunst/.config/dunst/dunstrc_preset',
]

if len(sys.argv) == 1:
    colormodn = 'defaultcolors'
else:
    colormodn = sys.argv[1]

colormod = importlib.import_module(colormodn)

for colorname, color in colormod.colors.items():
    colorformatted = formatColor(color, color)
    print(f'{colorname.rjust(15)}: {colorformatted}')

unused = set(colormod.colors.keys())

colre = re.compile('@(\w+)@')

if input('apply? ').startswith('y'):
    for conffilefname in files:
        with open(conffilefname, 'r') as f:
            conffcon = f.read()

        conffsub = conffcon

        for colname, color in colormod.colors.items():
            colorhex = rgbToHex(color)

            conffsubold = conffsub
            conffsub = conffsub.replace(f'@{colname}@', colorhex)

            if conffsubold != conffsub and colname in unused:
                unused.remove(colname)

        missing = set(colre.findall(conffsub))
        if len(missing):
            print(f'warning: missing colors in file {conffilefname}: ' + ', '.join(missing))

        with open(conffilefname.replace('_preset', ''), 'w') as f:
            f.write(conffsub)

    for unusedc in unused:
        print(f'warning: unused color \'{unusedc}\'')
