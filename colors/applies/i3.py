import utils

def apply(scheme, dotdir):
    with open(f'{dotdir}/i3/.config/i3/config.preset', 'r') as f:
        contents = f.read()

    contents = utils.findAdd(contents, '# I3 COLORS\n', scheme.i3Colors)

    with open(f'{dotdir}/i3/.config/i3/config', 'w') as f:
        f.write(contents)

def verify(scheme):
    return hasattr(scheme, 'i3Colors')
