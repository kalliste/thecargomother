
import os

basedir = ''

def set_basedir(set):
  global basedir
  basedir = set

# http://stackoverflow.com/questions/120656/directory-listing-in-python
def listdir_fullpath(d):
    return [os.path.join(d, f) for f in sorted(os.listdir(d))]

def load_sound_list(which):
  global basedir
  path = basedir + "/sounds/" + which
  ret = list()
  for file in listdir_fullpath(path): 
    if (file[-4:] == '.wav' or file[-4:] == '.ogg'):
      ret.append(file)
  return ret
