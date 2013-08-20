import random
from mplayer import Player
from util.media import *

def init():
  global vplayer
  global videos
  vplayer = Player(('-fs -fixed-vo'))
  videos = load_video_list("gathering/joey-usb/converted")

def event(num):
  global videos
  global vplayer
  vplayer.stop()
  vid = videos[num % len(videos)]
  vplayer.fullscreen = True
  print vid
  vplayer.loadfile(vid)

def tick():
  global vplayer
  x = vplayer.stream_pos
  if (vplayer.stream_end == None):
    event(random.randint(0,50))
  #print "pos: " + str(vplayer.stream_pos)
  #print "end: " + str(vplayer.stream_end)
