
import os,threading, time

def find_modes():
  ret = list()
  for file in sorted(os.listdir('modes')):
    if (file[-3:] == '.py' and file != '__init__.py'):
      ret.append(file[:-3])
  return ret

def load_mode(name):
  mod = __import__("modes." + name)
  return getattr(mod, name)

def setInterval(interval):
    def decorator(function):
        def wrapper(*args, **kwargs):
            stopped = threading.Event()

            def loop(): # executed in another thread
                while not stopped.wait(interval): # until stopped
                    function(*args, **kwargs)

            t = threading.Thread(target=loop)
            t.daemon = True # stop if the program exits
            t.start()
            return stopped
        return wrapper
    return decorator

def now():
  return time.mktime(time.gmtime()) 

def has_method(obj, method):
  try:
    dir(obj).index(method)
    return True
  except ValueError:
    pass
  return False

