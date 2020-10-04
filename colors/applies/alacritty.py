import utils

def apply(scheme, dotdir):
    with open(f'{dotdir}/alacritty/.config/alacritty/alacritty.yml', 'r') as f:
        contents = f.read()

    contents = utils.chunkOut(contents, '# COLORS START\n', '# COLORS END\n', scheme.alacrittyColors)

    with open(f'{dotdir}/alacritty/.config/alacritty/alacritty.yml', 'w') as f:
        f.write(contents)

def verify(scheme):
    return hasattr(scheme, 'alacrittyColors')
