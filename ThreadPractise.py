__author__ = 'fly'

import time
import urllib2
from threading import Thread

URLS = [
        'http://www.baidu.com',
        'http://www.qq.com',
        'http://www.taobao.com',
        'http://www.alibaba.com',
        'http://www.jd.com'
    ]

def get_responses():
    start = time.time()
    for url in URLS:
        print url
        resp = urllib2.urlopen(url)
        print resp.getcode()
    print "Elapsed time: %s" % (time.time()-start)

class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url
        super(GetUrlThread, self).__init__()
    def run(self):
        resp = urllib2.urlopen(self.url)
        print self.url, resp.getcode()

def get_responsesByMultiThread():
    start = time.time()
    threads = []
    for url in URLS:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print "Elapsed time: %s" % (time.time()-start)

get_responsesByMultiThread()
