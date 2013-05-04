import termios, sys, os, select, subprocess
from mplayer import Player

import random
import serial

total_palettes = 3 
total_video_files = 11
total_long_files = 8
button_order = [
 12,16,19,2, #  0  1  2  3
 13,3,5,10,  #  4  5  6  7
 6,0,17,9,   #  8  9 10 11
 11,1,18,14, # 12 13 14 15
 4,15        # 16 17
]

def shellquote(s):
    return "'" + s.replace("'", "'\\''") + "'"

def play_cmd(MEDIA):
  return 'mplayer ' + shellquote(MEDIA) + ' &>/dev/null </dev/null &'

def sound_file(palette, i):
  return 'clips/using-audio/' + str(palette) + '/clip' + str(i + 1) + '.wav'
 
def long_file(i):
  return 'clips/using-long/clip' + str(i) + '.wav'
 
def video_file(i):
  return 'clips/using-videos/' + str(i) + '.mp4'

def button_idx(button_order):
  idx = range(0,max(button_order)+1)
  for i in range(0,len(button_order)):
    idx[button_order[i]] = i
  return idx

def play_cmd(MEDIA):
  return 'mplayer ' + shellquote(MEDIA) + ' &>/dev/null </dev/null &'


idx = button_idx(button_order)
playerv=Player() #Player module only used for videos
ser = serial.Serial('/dev/ttyACM0',9600)
ser.readline() # toss one line so we are aligned
old_vals = vals = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
palette = palette_counter = 0
just_changed_palette = 0
while 1:
 x = ser.readline()
 vals = x.strip().split(',')
 print " "
 print old_vals
 print vals
 for i in range(0, len(vals)):
  if (int(vals[i]) == 1 and int(old_vals[i]) == 0):
   print "trigger " + str(i)
   if (i == 7):
    if (random.randint(0,1) == 0 or just_changed_palette == 1):
     just_changed_palette = 0
     playerv.stop()
     vid = video_file(random.randint(1,total_video_files))
     print vid
     playerv.loadfile(vid)
     playerv.fullscreen = True
    else:
     playerv.stop()
     playerv.loadfile(long_file(random.randint(1,total_long_files)))
     playerv.fullscreen = True
   elif (i == 8):
    palette_counter = palette_counter + 1
    palette = palette_counter % total_palettes
    just_changed_palette = 1
    print "counter is at " + str(palette_counter)
    print "palette is at " + str(palette)
   else:
    print sound_file(palette,idx[i])
    os.system(play_cmd(sound_file(palette,idx[i])))
 old_vals = vals
