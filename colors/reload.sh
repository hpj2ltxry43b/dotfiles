#!/usr/bin/bash

i3-msg restart

sleep 0.1 # yes i know this is bad but whatever
killall dunst

sleep 0.1
( dunst & )

for vs in $(vim --serverlist)
do
    vim --remote-send ':so $RC<CR>' --servername "$vs"
done
