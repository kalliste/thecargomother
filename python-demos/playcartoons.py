#!/usr/bin/python

class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()




import pygame

clips = list()
pygame.mixer.init()
for i in range(1, 27):
  clips.append(pygame.mixer.Sound("cartoon/cartoon%03d.wav" % i)) 
for i in range(27, 53):
  clips.append(pygame.mixer.Sound("musicalish/musical%03d.wav" % i)) 

keys = {
  'a':1,
  'b':2,
  'c':3,
  'd':4,
  'e':5,
  'f':6,
  'g':7,
  'h':8,
  'i':9,
  'j':10,
  'k':11,
  'l':12,
  'm':13,
  'n':14,
  'o':15,
  'p':16,
  'q':17,
  'r':18,
  's':19,
  't':20,
  'u':21,
  'v':22,
  'w':23,
  'x':24,
  'y':25,
  'z':26,
  'A':27,
  'B':28,
  'C':29,
  'D':30,
  'E':31,
  'F':32,
  'G':33,
  'H':34,
  'I':35,
  'J':36,
  'K':37,
  'L':38,
  'M':39,
  'N':40,
  'O':41,
  'P':42,
  'Q':43,
  'R':44,
  'S':45,
  'T':46,
  'U':47,
  'V':48,
  'W':49,
  'X':50,
  'Y':51,
  'Z':52
}

print "Ready"

import serial
ser = serial.Serial(port='/dev/tty.usbmodem1a21', baudrate=9600)
vals = old_vals = [0] * 52
while True:
  x = ser.readline()
  vals = x.strip().split(',') 
  for i in range(0, len(vals)):
    if (int(vals[i]) == 1 and int(old_vals[i]) == 0):
      print "trigger " + str(i)
      clips[i].play()

#while True:
#  clips[keys[getch()]].play()
