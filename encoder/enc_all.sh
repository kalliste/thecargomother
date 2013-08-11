#!/bin/bash
mkdir -p converted
for I in *; do ./enc.sh "$I" "converted/$I-vj.avi"; done
