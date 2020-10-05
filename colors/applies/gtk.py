import utils

def apply(scheme, dotdir):
    with open(f'{dotdir}/gtkrc/.gtkrc-2.0', 'w') as f:
        f.write(f'''
gtk-icon-theme-name = "{scheme.gtk2IconTheme}"
gtk-theme-name = "{scheme.gtk2Theme}"
gtk-font-name = "DejaVu Sans 11"
        ''')

    with open(f'{dotdir}/gtkrc/.config/gtk-3.0/settings.ini', 'w') as f:
        f.write(f'''
[Settings]
gtk-icon-theme-name = {scheme.gtk3IconTheme}
gtk-theme-name = {scheme.gtk3Theme}
gtk-font-name = DejaVu Sans 11
        ''')

def verify(scheme):
    return hasattr(scheme, 'gtk2Theme') and hasattr(scheme, 'gtk3Theme') and hasattr(scheme, 'gtk2IconTheme') and hasattr(scheme, 'gtk3IconTheme')
