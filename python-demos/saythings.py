#!/usr/bin/python

import pyttsx

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




#import pygame

#clips = list()
#pygame.mixer.init()
#for i in range(1, 27):
#  clips.append(pygame.mixer.Sound("cartoon/cartoon%03d.wav" % i)) 
#for i in range(27, 53):
#  clips.append(pygame.mixer.Sound("musicalish/musical%03d.wav" % i)) 

keys = {
  'a': 'I am a golden god',
  'b': 'Fuck',
  'c': 'Fuckstick',
  'd': 'Fucker',
  'e': 'Shit',
  'f': 'Cock',
  'g': 'Cockmonger',
  'h': 'Cocksucker',
  'i': 'Chode',
  'j': 'Shithead',
  'k': 'Dicks',
  'l': 'Cunt',
  'm': 'Lick my yarbles',
  'n': 'Rap',
  'o': 'Riddle',
  'p': 'Rat',
  'q': 'Please do not push this button again',
  'r': 'Rig',
  's': 'Sip',
  't': 'Sap',
  'u': 'Soap',
  'v': 'Sitting',
  'w': 'Sour',
  'x': 'Naps',
  'y': 'Nips',
  'z': 'Notes',
  'A': '',
  'B': '',
  'C': '',
  'D': '',
  'E': '',
  'F': '',
  'G': '',
  'H': '',
  'I': '',
  'J': '',
  'K': '',
  'L': '',
  'M': '',
  'N': '',
  'O': '',
  'P': '',
  'Q': '',
  'R': '',
  'S': '',
  'T': '',
  'U': '',
  'V': '',
  'W': '',
  'X': '',
  'Y': '',
  'Z': ''
}


print "Ready"

engine = pyttsx.init()


voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[len(voices) - 5].id)

while True:
  engine.say(keys[getch()], 'fox')
  engine.runAndWait()


#
#
#def onStart(name):
#   print 'starting', name
#def onWord(name, location, length):
#   print 'word', name, location, length
#def onEnd(name, completed):
#   print 'finishing', name, completed
#   if name == 'fox':
#      engine.say(keys[getch()], 'fox')
#   elif name == 'dog':
#      engine.endLoop()
#engine = pyttsx.init()
#engine.connect('started-utterance', onStart)
#engine.connect('started-word', onWord)
#engine.connect('finished-utterance', onEnd)
#engine.say('begin', 'fox')
#engine.startLoop()
#
