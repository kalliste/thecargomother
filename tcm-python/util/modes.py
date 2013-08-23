import os, random
from util.main import *

mode = None

def find_modes():
  static_list = [
    "espeak",
    "joeyvids",
    "peoplesounds",
    "soundeffects",
    "videoclips"
  ]
  return static_list
  ret = list()
  for file in sorted(os.listdir('modes')):
    if (file[-3:] == '.py' and file != '__init__.py'):
      ret.append(file[:-3])
  return ret

def load_mode(name):
  mode = __import__("modes." + name)
  return getattr(mode, name)

def go_mode_now(name):
  global mode
  global do_mode_change
  global selected_mode
  selected_mode = name
  do_mode_change = False
  if (has_method(mode, "deinit")):
    mode.deinit()
  mode = load_mode(name)
  mode.init()
  return mode

def mode_change_if_queued():
  global do_mode_change
  global selected_mode 
  global mode
  #print "mode change if needed"
  if (do_mode_change):
    #print "confirmed - do mode change"
    mode = go_mode_now(selected_mode)
  return mode

def go_next_mode():
  global selected_mode
  global do_mode_change
  modes = find_modes()
  idx = 0
  try:
    idx = modes.index(selected_mode)
  except ValueError:
    pass
  idx = idx + 1
  if (idx >= len(modes)):
    idx = 0
  selected_mode = modes[idx]
  do_mode_change = True
  print "selected mode: " + selected_mode

def go_random_mode():
  global selected_mode
  global do_mode_change
  modes = find_modes()
  selected_mode = modes[random.randint(0, len(modes)-1)]
  do_mode_change = True
  print "selected mode: " + selected_mode

