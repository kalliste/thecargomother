#!/usr/bin/python

import drivers.kbdriver as driver
#import drivers.serialdriver as driver

from util.main  import *
from util.media import *
from util.modes import *
from util.state import *

@setInterval(1)
def handle_periodic_events():
  global mode
  if (has_method(mode, 'tick')):
    try:
      mode.tick() 
    except:
      23
  if (since_last_event() > 10):
    # fire a random event if nothing has happened in the last minute
    print "idle"
    #mode.event(random.randint(0,50))

set_basedir(os.path.expanduser("~/videos-core"))
print "load and init mode"
mode = go_mode_now("peoplesounds")
mode.init()
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
