#!/usr/bin/python

from util.main  import *
from util.media import *
from util.modes import *
from util.state import *

from socket import *
hostname = gethostname()
if (hostname == 'familiar'):
  import drivers.kbdriver as driver
else:
  import drivers.serialdriver as driver

@setInterval(1)
def handle_periodic_events():
  global mode
  if (has_method(mode, 'tick')):
    try:
      mode.tick() 
    except:
      23
  if (since_last_event() > 10):
    23
    # fire a random event if nothing has happened in the last minute
    #print "idle"
    #mode.event(random.randint(0,50))

set_basedir(os.path.expanduser("~/videos-core"))
print "load and init mode"
mode = go_mode_now("hybrid")
driver.init()
last_event_now()
handle_periodic_events()
print "Ready"

while True:
  event = driver.get_event()
  if (type(event) == int):
    last_event_now()
    mode.event(event)
    mode = mode_change_if_queued()
  elif (event == '\x1b' or event == '\x03'):
    exit()
  else:
    if (len(event) == 1):
      print "'\\x" + event.encode('hex') + "'"
    else:
      print event
