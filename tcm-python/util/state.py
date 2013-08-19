
import time

def now():
  return time.mktime(time.gmtime()) 

def last_event_now():
  global last_event
  last_event = now()

def since_last_event():
  global last_event
  return now() - last_event

