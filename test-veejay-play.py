#!/usr/bin/python

#Simple script to call veejay through python and send it a video
#Second version: sends several VIMS commands

import subprocess
import time

POPEN=subprocess.Popen
PIPE=subprocess.PIPE
SLEEP=time.sleep

video = "sample-video.mov"
stream = POPEN("veejay " + video, shell=True)

SLEEP(5)

while True:
 SLEEP(3)
 sayv = POPEN("sayVIMS -m \"012:;\"", shell=True, stdout=PIPE) #Pause
 SLEEP(3)
 sayv = POPEN("sayVIMS -m \"011:;\"", shell=True, stdout=PIPE) #Play Backwards
 SLEEP(3)
 sayv = POPEN("sayVIMS -m \"012:;\"", shell=True, stdout=PIPE) #Pause
 SLEEP(3)
 sayv = POPEN("sayVIMS -m \"010:;\"", shell=True, stdout=PIPE) #Play Forwards
