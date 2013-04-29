#!/usr/bin/python

import sys, os
import urlparse
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

		print "[i] Saving/Updating fiddle: " + fiddles[index]["title"] + "... "
		stash(fiddles[index]["title"], fiddles[index]["latest_version"], fiddles[index]["url"], fiddles[index]["description"])

	print "[i] All Backed Up!"
	return

def stash(title, version, url, description):


	for i in range(version):

		#make url
		urllist = urlparse.urlsplit(url)
		ulist = list(urllist)

		h = ulist[0].replace('http', 'http://')
		p = ulist[1].replace('jsfiddle.net', 'fiddle.jshell.net')
		v = ulist[3].replace('', str(i))
		s = ulist[4].replace('', '/show/light/')

		ulist[0] = h
		ulist[1] = p
		ulist[3] = v
		ulist[4] = s

		ourl = ''.join(ulist)

		page = urllib2.Request(ourl)
		response = urllib2.urlopen(page)
		the_page = response.read()

		#make main directory
		if not os.path.exists('fiddles'):
		    os.makedirs('fiddles')

		#make sub directory
		if not os.path.exists('fiddles/' + title + '/' + str(i)):
		    os.makedirs('fiddles/' + title + '/' + str(i))

		#make readme file
		path = "fiddles/" + title + '/' + str(i) + "/README.md"
		f = open(path, 'w+')
		f.write("##" + title + "\nDescription: " + description + "\nVersions: " + str(i) + "\nurl: " + url)
		f.close()

		#make version files
		path = "fiddles/" + title + '/' + str(i) + "/index.html"
		f = open(path, 'w+')
		f.write(the_page)
		f.close()

if __name__ == "__main__":
   main(sys.argv[1:])