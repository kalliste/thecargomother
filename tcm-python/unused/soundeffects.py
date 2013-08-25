#!/usr/bin/python

import os, random
from util.media import *

def init():
  global clips
  clips = load_sound_list("cartoon")

def event(num):
  global clips
  clip = clips[num % len(clips)]
  cmd = 'aplay ' + clip + ' -D plug:dmix -q &'
  os.system(cmd)
