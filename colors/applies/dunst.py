import utils

def apply(scheme, dotdir):
    with open(f'{dotdir}/dunst/.config/dunst/dunstrc', 'r') as f:
        contents = f.read()

    colors = '''    background = "{}"
    foreground = "{}"
'''

    lowurgencycolors = colors.format(*scheme.dunstLow)
    normalurgencycolors = colors.format(*scheme.dunstNormal)
    criticalurgencycolors = colors.format(*scheme.dunstCritical)

    contents = utils.chunkOut(contents, '# DUNST LOW URGENCY BEGIN\n'     , '    # DUNST LOW URGENCY END'     , lowurgencycolors     )
    contents = utils.chunkOut(contents, '# DUNST NORMAL URGENCY BEGIN\n'  , '    # DUNST NORMAL URGENCY END'  , normalurgencycolors  )
    contents = utils.chunkOut(contents, '# DUNST CRITICAL URGENCY BEGIN\n', '    # DUNST CRITICAL URGENCY END', criticalurgencycolors)

    with open(f'{dotdir}/dunst/.config/dunst/dunstrc', 'w') as f:
        f.write(contents)

def verify(scheme):
    return hasattr(scheme, 'dunstLow') and hasattr(scheme, 'dunstNormal') and hasattr(scheme, 'dunstCritical')
