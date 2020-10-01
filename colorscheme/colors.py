import json
import sys
import re

def formatColor(color, text):
    colorr, colorg, colorb = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)

    fcolor = 30 if colorr + colorg + colorb > 381 else 37

    return f'\033[48;2;{colorr};{colorg};{colorb}m\033[{fcolor}m{text}\033[0m'

def resolveColor(color):
    if color.startswith('#'):
        return color, color
    elif color.startswith('@'):
        resolved = resolveColor(colors[color[1:]])
        return color + ' -> ' + resolved[0], resolved[1]

files = [
    '../alacritty/.config/alacritty/alacritty_preset.yml',
    '../i3/.config/i3/config_preset',
    '../bin/bin/lock_preset.sh',
    '../dunst/.config/dunst/dunstrc_preset',
]
if len(sys.argv) == 1:
    colorfilepath = 'colors.json'
else:
    colorfilepath = sys.argv[1]

with open(colorfilepath, 'r') as f:
    colors = json.load(f)

for colorname in colors:
    resolvechain, colresolved = resolveColor(colors[colorname])
    colorformatted = formatColor(colresolved, resolvechain)
    print(f'{colorname.rjust(15)}: {colorformatted}')

colre = re.compile('@(\w+)@')
if input('apply? ').startswith('y'):
    for conffilefname in files:
        with open(conffilefname, 'r') as f:
            conffcon = f.read()

        conffsub = conffcon

        for colname in colors:
            _, colres = resolveColor(colors[colname])
            conffsub = conffsub.replace(f'@{colname}@', colres)

        missing = colre.findall(conffsub)
        if len(missing):
            print(f'warning: missing colors in file {conffilefname}: ' + ', '.join(missing))
            if not input('write? ').startswith('y'):
                continue

        with open(conffilefname.replace('_preset', ''), 'w') as f:
            f.write(conffsub)

