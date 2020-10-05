import utils

def apply(scheme, dotdir):
    with open(f'{dotdir}/dunst/.config/dunst/dunstrc.preset', 'r') as f:
        contents = f.read()

    colors = '''    background = "{}"
    foreground = "{}"
'''

    lowurgencycolors = colors.format(*scheme.dunstLow)
    normalurgencycolors = colors.format(*scheme.dunstNormal)
    criticalurgencycolors = colors.format(*scheme.dunstCritical)

    contents = utils.findAdd(contents, '# DUNST LOW URGENCY\n'     , lowurgencycolors     )
    contents = utils.findAdd(contents, '# DUNST NORMAL URGENCY\n'  , normalurgencycolors  )
    contents = utils.findAdd(contents, '# DUNST CRITICAL URGENCY\n', criticalurgencycolors)

    with open(f'{dotdir}/dunst/.config/dunst/dunstrc', 'w') as f:
        f.write(contents)

def verify(scheme):
    return hasattr(scheme, 'dunstLow') and hasattr(scheme, 'dunstNormal') and hasattr(scheme, 'dunstCritical')
