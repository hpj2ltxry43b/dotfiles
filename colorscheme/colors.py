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
    ('../alacritty/.config/alacritty/alacritty_preset.yml', '../alacritty/.config/alacritty/alacritty.yml'),
    ('../i3/.config/i3/config_preset', '../i3/.config/i3/config'),
    ('../bin/bin/lock_preset.sh', '../bin/bin/lock.sh'),
    ('../dunst/.config/dunst/dunstrc_preset', '../dunst/.config/dunst/dunstrc'),
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
    for conffilefnamein, confffilefnameout in files:
        with open(conffilefnamein, 'r') as f:
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

        with open(conffilefnameout, 'w') as f:
            f.write(conffsub)

    for unusedc in unused:
        print(f'warning: unused color \'{unusedc}\'')
