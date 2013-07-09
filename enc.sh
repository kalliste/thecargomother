#!/bin/sh

usage() {
  echo "Usage: $0 filename"
  exit 1
}
 
is_file_exits() {
  local f="$1"
  [[ -f "$f" ]] && return 0 || return 1
}

[[ $# -eq 0 ]] && usage
 
if ( is_file_exits "$1" )
then
  ff=$1
  filename=$(basename $ff)
  extension=${filename##*.}
  filename=${filename%.*}
  
  mkdir -p converted
  ffmpeg -i "${ff}"  -vf "scale=512:384" -r 24 -an -pix_fmt yuvj420p -vcodec mjpeg -f mov -y converted/"${filename}"-vj.mov
else
 echo "File not found"
fi


