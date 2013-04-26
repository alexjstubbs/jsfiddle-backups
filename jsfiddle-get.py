#!/usr/bin/python

import sys, os
import re
import urlparse
from bs4 import BeautifulSoup
import urllib2

#common messages
n1 = "[!] Already Exists! Update your fiddle then run command on new url"
n2 = "[i] Making Directory: "
n3 = "[i] Crawling Fiddle..."
n4 = "[i] Saving Original Fiddle..."
#get arguments and build base url
url = sys.argv[1];
urllist = urlparse.urlsplit(url)
ulist = list(urllist)

#replace parts of url
h = ulist[0].replace('http', 'http://')
p = ulist[1] = 'fiddle.jshell.net'
t = ulist[2].replace('embedded/result', 'show/light')

ulist[0] = h
ulist[2] = t

#join url
ourl = ''.join(ulist)

#make directories
if not os.path.exists('fiddles'):
    os.makedirs('fiddles')
    print n2 + '/fiddles'

dir_ = ulist[2].rsplit('/')[2] + "/" + ulist[2].rsplit('/')[3]

if not os.path.exists('fiddles/' + dir_):
	print n2 + dir_
	os.makedirs("fiddles/" + dir_)

else:
	print n1 
	exit()


#Crawl page
print n3
#page = urllib2.urlopen(ourl)
page = urllib2.Request(ourl)
response = urllib2.urlopen(page)
the_page = response.read()

#Save Original
print n4
path = "fiddles/" + dir_ + "/index.html"
f = open(path, 'w+')

f.write(the_page)
f.close()


