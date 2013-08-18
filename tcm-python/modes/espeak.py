
import os
import random


def init(_util):
  global phrases
  phrases = util.media.load_text_set("set1"):

def event(num):
  global phrases
  phrase = phrases[num % len(phrases)]
  cmd = 'espeak "' + phrase + '" --stdout | aplay -q &'
  #print cmd
  os.system(cmd)

def tick():
  event(random.randint(0,50))
