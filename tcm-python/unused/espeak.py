
import os, random
from util.media import *

def init():
  global phrases
  phrases = load_text_set("set1")

def event(num):
  global phrases
  phrase = phrases[num % len(phrases)]
  cmd = 'espeak "' + phrase + '" --stdout | aplay -D plug:dmix -q &'
  #print cmd
  os.system(cmd)

def tick():
  event(random.randint(0,50))
