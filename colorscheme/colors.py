import json
import sys
import re
import colorsys

def formatColor(color, text):
    colorr, colorg, colorb = hexToRgb(color)

    fcolor = 30 if colorr + colorg + colorb > 381 else 37

    return f'\033[48;2;{colorr};{colorg};{colorb}m\033[{fcolor}m{text}\033[0m'

def resolveColor(color):
    if color.startswith('#'):
        return color
    elif color.startswith('@'):
        resolved = resolveColor(colors[color[1:]])
        return resolved
    elif color.startswith('$'):
        func, val = color.split(' ', 1)
        colorAsHex = resolveColor(val)

        if func == '$lighten':
            colhls = list(colorsys.rgb_to_hls(*hexToRgb(colorAsHex)))
            colhls[1] += 50
            return rgbToHex(clampRGB(colorsys.hls_to_rgb(*colhls)))

        elif func == '$darken':
            colhls = list(colorsys.rgb_to_hls(*hexToRgb(colorAsHex)))
            colhls[1] -= 50
            return rgbToHex(clampRGB(colorsys.hls_to_rgb(*colhls)))

        else:
            raise Exception(f'invalid function \'{func}\'')

def hexToRgb(hexc):
    return (int(hexc[1:3], 16), int(hexc[3:5], 16), int(hexc[5:7], 16))

def rgbToHex(rgbc):
    return '#' + hex(int(rgbc[0]))[2:].zfill(2) + hex(int(rgbc[1]))[2:].zfill(2) + hex(int(rgbc[2]))[2:].zfill(2)

def clampRGB(rgbc):
    return tuple(min(255, max(x, 0)) for x in rgbc)

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
    colresolved = resolveColor(colors[colorname])
    colorformatted = formatColor(colresolved, colresolved)
    print(f'{colorname.rjust(15)}: {colorformatted}')

unused = set(colors.keys())
colre = re.compile('@(\w+)@')
if input('apply? ').startswith('y'):
    for conffilefname in files:
        with open(conffilefname, 'r') as f:
            conffcon = f.read()

        conffsub = conffcon

        for colname in colors:
            colres = resolveColor(colors[colname])
            conffsubold = conffsub
            conffsub = conffsub.replace(f'@{colname}@', colres)
            if conffsubold != conffsub and colname in unused:
                unused.remove(colname)

        missing = colre.findall(conffsub)
        if len(missing):
            print(f'warning: missing colors in file {conffilefname}: ' + ', '.join(missing))
            if not input('write? ').startswith('y'):
                continue

        with open(conffilefname.replace('_preset', ''), 'w') as f:
            f.write(conffsub)


    for unusedc in unused:
        print(f'warning: unused color \'{unusedc}\'')
