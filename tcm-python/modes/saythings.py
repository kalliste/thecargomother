
type = 'text'

import pyttsx

engine = None

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
  global engine 
  global util
  util = _util
  engine = pyttsx.init()

def event(num):
  global engine
  engine.say(phrases[num % len(phrases)], 'myphrase')
  engine.runAndWait()
