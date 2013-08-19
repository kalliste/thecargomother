#!/usr/bin/python

import Queue
import threading
import urllib2

# called by each thread
def get_url(q, url):
    q.put(urllib2.urlopen(url).read())

theurls = '''http://google.com http://yahoo.com'''.split()

q = Queue.Queue()

for a_url in theurls:
    t = threading.Thread(target=get_url, args = (q, a_url))
    t.daemon = True
    t.start()

s = q.get()
print s
