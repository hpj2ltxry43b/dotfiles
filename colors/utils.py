import colorsys

def chunkOut(contents, startmarker, endmarker, replacement):
    contents = str(contents)
    startin = contents.find(startmarker)
    endin   = contents.find(endmarker  )

    if startin == -1:
        raise Exception(f'Start marker {startmarker} not found in contents')

    if endin == -1:
        raise Exception(f'End marker {endmarker} not found in contents')

    contents = contents[:startin + len(startmarker)] + replacement + contents[endin:]

    return contents

def findAdd(contents, marker, addition):
    contents = str(contents)
    addin = contents.find(marker)

    if addin == -1:
        raise Exception(f'Marker {marker} not found in contents')

    contents = contents[:addin + len(marker)] + addition + contents[addin + len(marker):]

    return contents

def lighten(r, g, b, amt):
    colhls = list(colorsys.rgb_to_hls(r, g, b))
    colhls[1] += amt
    return clampRGB(*integerize(*colorsys.hls_to_rgb(*colhls)))

def darken(r, g, b, amt):
    colhls = list(colorsys.rgb_to_hls(r, g, b))
    colhls[1] -= amt
    return clampRGB(*integerize(*colorsys.hls_to_rgb(*colhls)))

def lightenHex(hexc, amt):
    return RGBToHex(lighten(*hexToRGB(hexc), amt))

def darkenHex(hexc, amt):
    return RGBToHex(darken(*hexToRGB(hexc), amt))

def integerize(r, g, b):
    return (int(r), int(g), int(b))

def clampRGB(r, g, b):
    return tuple(min(255, max(c, 0)) for c in (r, g, b))

def hexToRGB(hexc):
    return (int(hexc[1:3], 16), int(hexc[3:5], 16), int(hexc[5:7], 16))

def RGBToHex(rgbc):
    return '#' + ''.join(hex(c)[2:].zfill(2) for c in rgbc)
