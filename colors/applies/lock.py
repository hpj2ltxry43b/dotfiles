
def apply(scheme, dotdir):
    with open(f'{dotdir}/bin/bin/lock.sh', 'w') as f:
        f.write(f'i3lock -ef -c "{scheme.lockColor}"')

def verify(scheme):
    return hasattr(scheme, 'lockColor')
