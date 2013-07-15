%module veejay

%{
#define SWIG_FILE_WITH_INIT
#include "veejay.h"
%}

%include "veejay.h"

%pythoncode %{

import subprocess

def launch_server(start_vid):
  stream = subprocess.Popen("veejay " + start_vid, shell=True)

def kill_servers():
  stream = subprocess.Popen("killall -9 veejay ", shell=True)

%}
