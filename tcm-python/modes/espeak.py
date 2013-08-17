
import os

type = 'text'

phrases = [
  'I am a golden god',
  'Fuck',
  'Fuckstick',
  'Fucker',
  'Shit',
  'Cock',
  'Cockmonger',
  'Cocksucker',
  'Chode',
  'Shithead',
  'Dicks',
  'Cunt',
  'Lick my yarbles',
  'Rap',
  'Riddle',
  'Rat',
  'Please do not push this button again',
  'Rig',
  'Sip',
  'Sap',
  'Soap',
  'Sitting',
  'Sour',
  'Naps',
  'Nips',
  'Notes'
]

def init(_util):
  23

def event(num):
  global phrases
  phrase = phrases[num % len(phrases)]
  cmd = 'espeak "' + phrase + '" --stdout | aplay -q &'
  print cmd
  os.system(cmd)
