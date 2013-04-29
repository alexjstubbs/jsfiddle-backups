#!/usr/bin/python

import sys, os
import re
import urlparse
from bs4 import BeautifulSoup
import urllib2
import simplejson as json


def main(argv):
	#get arguments and build base url
	if len(sys.argv) == 1:
		print "[!] No username specified!"
		exit()
	else:
		user = sys.argv[1];

	obj = "http://jsfiddle.net/api/user/" + user + "/demo/list.json"

	fiddles = json.load(urllib2.urlopen(obj))

	for index, item in enumerate(fiddles):

		stash(fiddles[index]["title"], fiddles[index]["version"], fiddles[index]["url"], fiddles[index]["description"])

	return

def stash(title, version, url, description):

	#make main directory
	if not os.path.exists('fiddles'):
	    os.makedirs('fiddles')
	    print "[i] Creating Directory: " + 'fiddles'	

	#make sub directory
	if not os.path.exists('fiddles/' + title):
	    os.makedirs('fiddles/' + title)
	    print "[i] Creating Directory: " + 'fiddles/' + title

	#make readme file
	path = "fiddles/" + title + "/readme.md"
	f = open(path, 'w+')
	f.write("##" + title + " (version: " + str(version) + ")\n" + description)
	f.close()

	#make url
	urllist = urlparse.urlsplit(url)
	ulist = list(urllist)


	h = ulist[0].replace('http', 'http://')
	p = ulist[1].replace('jsfiddle.net', 'fiddle.jshell.net')
	s = ulist[3].replace('', 'show/light/')

	# t = ulist[2].replace('embedded/result', 'show/light')

	ulist[0] = h
	ulist[1] = p
	ulist[3] = s;

	ourl = ''.join(ulist)

	page = urllib2.Request(ourl)
	response = urllib2.urlopen(page)
	the_page = response.read()

	path = "fiddles/" + title + "/index.html"
	f = open(path, 'w+')
	f.write(the_page)
	f.close()

	print "[i] Saved fiddle: " + title


if __name__ == "__main__":
   main(sys.argv[1:])