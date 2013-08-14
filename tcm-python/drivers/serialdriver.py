import Queue
import re
import os
import serial

def init():
  global ser
  global old_vals
  global vals
  global q
  q = Queue.Queue()
  old_vals = vals = ['0'] * 52
  device = ''
  for a_device in os.listdir("/dev"):
    if (re.match('tty.usbmodem', a_device) or re.match('ttyACM', a_device)):
      device = "/dev/" + a_device
  ser = serial.Serial(device, 9600)
  ser.readline() # toss one line so we are aligned

def get_event():
  global ser
  while (q.qsize() == 0):
    x = ser.readline()
    vals = x.strip().split(',')
    for i in range(0, len(vals)):
      if (int(vals[i]) == 1 and int(old_vals[i]) == 0):
        q.put(i)
  if (q.qsize() != 0):
    ret = q.get()
    return ret
