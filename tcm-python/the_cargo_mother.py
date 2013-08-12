#!/usr/bin/python

import drivers.kbdriver as driver

import os

def find_modes():
  ret = list()
  for file in sorted(os.listdir('modes')):
    if (file[-3:] == '.py' and file != '__init__.py'):
      ret.append(file[:-3])
  return ret

def load_mode(name):
  mod = __import__("modes." + name)
  return getattr(mod, name)

import util.media
util.media.set_basedir(os.path.expanduser("~/videos-core"))

modes = find_modes()
mode = load_mode(modes[1])
mode.init(util)

driver.init()

print "Ready"
while True:
  event = driver.get_event()
  if (event >= 0):
    mode.event(event)
