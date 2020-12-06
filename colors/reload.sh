#!/usr/bin/bash

for vs in $(vim --serverlist)
do
    vim --remote-send ':so $RC<CR>' --servername "$vs"
done
