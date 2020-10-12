import -window root /tmp/lock.jpg
convert /tmp/lock.jpg -scale 5% -scale 2000% /tmp/lock.png
i3lock -ef -i /tmp/lock.png
