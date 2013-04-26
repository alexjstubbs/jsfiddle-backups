#!/usr/bin/python

import sys, os
import re
import urlparse
from bs4 import BeautifulSoup
import urllib2

#get arguments and build base url
url = sys.argv[1];
urllist = urlparse.urlsplit(url)
ulist = list(urllist)

h = ulist[0].replace('http', 'http://')
p = ulist[1] = 'fiddle.jshell.net'
t = ulist[2].replace('embedded/result', 'show/light')

ulist[0] = h
ulist[2] = t

ourl = ''.join(ulist)

#make directory

os.makedirs("fiddles/" + ulist[2].rsplit('/')[2])

#Crawl page
page = urllib2.urlopen(ourl)
