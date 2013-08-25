import veejay, time

def init():
  global ready
  ready = False
  file = '/home/hacker/videos-core/gathering/joey-usb/converted/Vade_-_My_Prophet_is_a_Word_not_Known.mov-vj.avi'
  veejay.kill_servers()
  time.sleep(0.5)
  veejay.launch_server(file)

def event(num):
  global ready
  commands = [
    "010:;",
    "011:;",
    "012:;",
  ]
  if (ready):
    cmd = commands[num % len(commands)]
    veejay.command(cmd)

def tick():
  global ready
  if (not ready):
    if (veejay.conn_open() == 0):
      ready = True
