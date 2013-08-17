#!/usr/bin/python

import drivers.kbdriver as driver
#import drivers.serialdriver as driver

import util.media

from util.main import *

def last_event_now():
  global last_event
  last_event = now()

@setInterval(1)
def handle_periodic_events():
  global last_event
  global mode
  if (has_method(mode, 'tick')):
    try:
      mode.tick() 
    except:
      23
  if (now() >= last_event + 2):
    # fire a random event if nothing has happened in the last minute
    last_event_now()
    #mode.event(random.randint(0,50))

util.media.set_basedir(os.path.expanduser("~/videos-core"))

modes = find_modes()
print "load and init mode"
#mode = load_mode(modes[1])
mode = load_mode("espeak")
#mode = load_mode("soundeffects")
mode.init(util)

driver.init()

last_event_now()
handle_periodic_events()
print "Ready"
while True:
  event = driver.get_event()
  if (type(event) == int):
    last_event_now()
    mode.event(event)
  elif (event == '\x1b' or event == '\x03'):
    exit()
  else:
    if (len(event) == 1):
      print "'\\x" + event.encode('hex') + "'"
    else:
      print event
