
def apply(scheme, dotdir):
    with open(f'{dotdir}/vim/.vim/curcolor.vim', 'w') as f:
        f.write(f'colo {scheme.vimColo}\n')

def verify(scheme):
    return hasattr(scheme, 'vimColo')
