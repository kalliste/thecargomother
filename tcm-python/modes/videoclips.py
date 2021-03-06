import random
from mplayer import Player
from util.media import *
from util.modes import *

def init():
  global vplayer
  global videos
  vplayer = Player(('-fs -fixed-vo'))
  videos = load_video_list("regularplay") + load_video_list("musicvid") + load_video_list("important")
  random.shuffle(videos)

def deinit():
  global vplayer
  vplayer.quit()

def event(num):
  global videos
  global vplayer
  if (random.randint(0, 25) == 23):
    go_random_mode()
  if (num == 0):
    print "vid go random mode"
    go_random_mode()
  else:
    vplayer.stop()
    vid = videos[num % len(videos)]
    vplayer.fullscreen = True
    print vid
    vplayer.loadfile(vid)

def tick():
  global vplayer
  if (random.randint(0, 1200) == 23):
    random.shuffle(videos)
  x = vplayer.stream_pos
  if (vplayer.stream_end == None):
    event(random.randint(0,50))
  #print "pos: " + str(vplayer.stream_pos)
  #print "end: " + str(vplayer.stream_end)
