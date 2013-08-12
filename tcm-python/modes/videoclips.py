from mplayer import Player

def init(util):
  global vplayer
  global videos
  vplayer = Player()
  videos = util.media.load_video_list("ftp")

def event(num):
  global videos
  vplayer.stop()
  vid = videos[num % len(videos)]
  vplayer.fullscreen = True
  vplayer.loadfile(vid)
