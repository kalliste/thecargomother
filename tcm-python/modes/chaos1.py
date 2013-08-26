import os, random, time
from mplayer import Player
from util.media import *
from util.modes import *

def init():
  global vplayer
  global videos
  global current_vid
  vplayer = Player(('-fs -fixed-vo'))
  videos = load_video_list("systemchaos")
  random.shuffle(videos)
  current_vid = 0
  play_vid(current_vid)
  
def play_vid(which):
  global vplayer
  global videos
  vplayer.stop()
  vplayer.loadfile(videos[which])

def deinit():
  global vplayer
  vplayer.quit()

def event(num):
  global videos
  mod = len(videos) + 1
  if (num % mod == mod - 1):
    go_random_mode()
  else:
    play_vid(num % mod)

def tick():
  global vplayer
  global videos
  global current_vid
  x = vplayer.stream_pos
  if (vplayer.stream_end == None):
    current_vid = current_vid + 1
    if (current_vid < len(videos)):
      play_vid(current_vid)
    else:
      go_random_mode()
