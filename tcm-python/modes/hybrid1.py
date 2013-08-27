import os, random, time
from mplayer import Player
from util.media import *
from util.modes import *

def init():
  global vplayer
  global videos
  global phrases
  phrases = load_text_set("burn1") + load_text_set("cursing") + load_text_set("daniel") + load_text_set("jewelz")
  random.shuffle(phrases)
  vplayer = Player(('-fs -fixed-vo'))
  videos = load_video_list("shortsilent")
  play_random_vid()

def play_random_vid():
  global vplayer
  global videos
  num = random.randint(0, len(videos)-1)
  vid = videos[num]
  vplayer.stop()
  print vid
  vplayer.loadfile(vid)

def deinit():
  global vplayer
  vplayer.quit()

def event(num):
  global phrases
  if (random.randint(0, 25) == 23):
    go_random_mode()
  phrase = phrases[num % len(phrases)]
  say_phrase(phrase)

def tick():
  global vplayer
  x = vplayer.stream_pos
  if (vplayer.stream_end == None):
    play_random_vid()

