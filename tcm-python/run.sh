#!/bin/bash
cd /home/hacker
while true; do 
  pkill mplayer
  pkill -9 veejay
  pkill the_cargo_mother
  python /home/hacker/thecargomother/tcm-python/the_cargo_mother.py
  sleep 10
done
