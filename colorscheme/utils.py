import colorsys

def lighten(r, g, b, amt):
    colhls = list(colorsys.rgb_to_hls(r, g, b))
    colhls[1] += amt
    return clampRGB(*colorsys.hls_to_rgb(*colhls))

def darken(r, g, b, amt):
    colhls = list(colorsys.rgb_to_hls(r, g, b))
    colhls[1] -= amt
    return clampRGB(*colorsys.hls_to_rgb(*colhls))

def clampRGB(r, g, b):
    return tuple(min(255, max(c, 0)) for c in (r, g, b))

def integerizeColors(colors):
    out = {}
    for colorn, (colorr, colorg, colorb) in colors.items():
        out[colorn] = (int(colorr), int(colorg), int(colorb))

    return out
