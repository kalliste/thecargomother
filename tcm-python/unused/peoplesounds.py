#!/usr/bin/python

import os, random
from util.media import *

def init():
  global clips
  global palette
  palette = 1
  clips = load_sound_list("people/sub" + str(palette))

def event(num):
  global clips
  global palette
  if (num == 0):
    if (palette == 8):
      palette = 0
    else:
      palette = palette + 1
    cmd = 'espeak "next set" --stdout | aplay -D plug:dmix -q &'
  else:
    clip = clips[num % len(clips)]
    cmd = 'aplay ' + clip + ' -D plug:dmix -q &'
  os.system(cmd)
