
def apply(scheme, dotdir):
    with open(f'{dotdir}/bin/bin/lock.sh', 'w') as f:
        f.write(f'import -window root /tmp/lock.jpg\n')
        f.write(f'convert /tmp/lock.jpg -scale 5% -scale 2000% /tmp/lock.png\n')
        f.write(f'i3lock -ef -i /tmp/lock.png\n')

def verify(scheme):
    return hasattr(scheme, 'lockColor')
