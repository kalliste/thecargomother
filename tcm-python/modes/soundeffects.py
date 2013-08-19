#!/usr/bin/python

import pygame
from util.media import *

def init():
  global clips
  pygame.mixer.init()
  clips = list()
  for file in load_sound_list("cartoon"):
    clips.append(pygame.mixer.Sound(file))

def event(num):
  global clips
  clips[num % len(clips)].play()
