#!/bin/bash

usage() {
  echo "Usage: $0 input_file output_file"
  exit 1
}
 
is_file_exits() {
  local f="$1"
  [[ -f "$f" ]] && return 0 || return 1
}

[[ $# -eq 0 ]] && usage
[[ $# -eq 1 ]] && usage
 
if ( is_file_exits "$1" )
then
  ffmpeg -i "$1"  -vf "scale=512:384" -r 24 -acodec pcm_s16le -pix_fmt yuvj420p -vcodec mjpeg -y "$2"
else
 echo "File not found"
fi


