#!/usr/bin/python

import drivers.kbdriver as driver
#import drivers.serialdriver as driver

import os, threading, time, random
import util.media

def find_modes():
  ret = list()
  for file in sorted(os.listdir('modes')):
    if (file[-3:] == '.py' and file != '__init__.py'):
      ret.append(file[:-3])
  return ret

def load_mode(name):
  mod = __import__("modes." + name)
  return getattr(mod, name)

def setInterval(interval):
    def decorator(function):
        def wrapper(*args, **kwargs):
            stopped = threading.Event()

            def loop(): # executed in another thread
                while not stopped.wait(interval): # until stopped
                    function(*args, **kwargs)

            t = threading.Thread(target=loop)
            t.daemon = True # stop if the program exits
            t.start()
            return stopped
        return wrapper
    return decorator

def now():
  return time.mktime(time.gmtime()) 

def last_event_now():
  global last_event
  last_event = now()

@setInterval(1)
def handle_periodic_events():
  global last_event
  global mode
  # fire a random event if nothing has happened in the last minute
  if (now() >= last_event + 2):
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
