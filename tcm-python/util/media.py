
import os, string

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

def load_video_list(which):
  global basedir
  path = basedir + "/videos/" + which
  ret = list()
  for file in listdir_fullpath(path): 
    if (file[-4:] == '.mp4' or file[-4:] == '.avi' or file[-4:] == '.flv'):
      ret.append(file)
  return ret

def load_text_set(which):
  global basedir
  fp = open(basedir + '/text/' + which + '.txt')
  lines = fp.readlines()
  fp.close()
  for (i, item) in enumerate(lines):
    lines[i] = string.strip(lines[i])
  return lines
