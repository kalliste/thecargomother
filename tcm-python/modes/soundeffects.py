#!/usr/bin/python

import pygame

clips = list()

def init(util):
  global clips
  pygame.mixer.init()
  for file in util.media.load_sound_list("cartoon"):
    clips.append(pygame.mixer.Sound(file))

def event(num):
  clips[num % len(clips)].play()
