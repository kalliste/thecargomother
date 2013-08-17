#!/bin/bash
mkdir -p converted
for I in *.gif; do
  mencoder -vf scale=512:384 -ovc lavc -lavcopts vcodec=mjpeg -o converted/"$I"-converted.avi "$I"
done
