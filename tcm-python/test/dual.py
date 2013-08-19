#!/usr/bin/python

import Queue, threading, sys, time, select
from socket import *

bufferSize = 1024 # whatever you need
MYPORT = 50000

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('<broadcast>', MYPORT))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.setblocking(0)

def watch_socket(q):
  while True:
    result = select.select([s],[],[])
    msg = result[0][0].recv(bufferSize) 
    print msg


q = Queue.Queue()
t = threading.Thread(target=watch_socket, args = (q,))
t.daemon = True
t.start()


hostname = gethostname()
while 1:
    data = hostname + ' ' + repr(time.time())
    s.sendto(data, ('<broadcast>', MYPORT))
    time.sleep(2)
