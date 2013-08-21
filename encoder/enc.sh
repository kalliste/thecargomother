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
  ffmpeg -i "$1" -r 24 -pix_fmt yuvj420p -vcodec mjpeg -acodec pcm_u8 -vf "scale=iw*min(640/iw\,480/ih):ih*min(640/iw\,480/ih),pad=640:480:(640-iw)/2:(480-ih)/2" -y "$2"
else
 echo "File not found"
fi


