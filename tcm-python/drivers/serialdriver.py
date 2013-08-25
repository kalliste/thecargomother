import Queue
import re
import os
import serial

def init():
  global ser
  global vals
  global old_vals
  global q
  global exceptions
  exceptions = 0
  q = Queue.Queue()
  old_vals = vals = ['0'] * 54
  device = ''
  for a_device in os.listdir("/dev"):
    if (re.match('tty.usbmodem', a_device) or re.match('ttyACM', a_device)):
      device = "/dev/" + a_device
  ser = serial.Serial(device, 9600)
  ser.readline() # toss one line so we are aligned

def get_event():
  global ser
  global vals
  global old_vals
  global q
  global exceptions
  while (q.qsize() == 0):
    try:
      x = ser.readline()
      vals = x.strip().split(',')
      for i in range(0, len(vals)):
        if (int(vals[i]) == 1 and int(old_vals[i]) == 0):
          q.put(i)
      old_vals = vals
    except:
      exceptions = exceptions + 1
      if (exceptions > 10):
        exit()
  if (q.qsize() != 0):
    ret = q.get()
    return ret
