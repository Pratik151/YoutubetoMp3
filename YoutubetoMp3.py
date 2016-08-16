#!/usr/bin/python2.7
import urllib2
import os
import pwd
import json
import sys


if len(sys.argv) < 2 or len(sys.argv) > 4:
   print "Usage: python YoutubetoMp3.py URL [path] [filename]"
   exit(0)
urlLink = 'http://www.youtubeinmp3.com/fetch/?format=JSON&video=' + sys.argv[1]
path = os.path.join('/home',pwd.getpwuid(os.getuid()).pw_name,'Music')
response = urllib2.urlopen(urlLink)
data = json.load(response)
downloadLink = data['link']
print downloadLink
title = data['title']
filename = title + '.mp3'
if len(sys.argv) == 3:
   path = sys.argv[2]
elif len(sys.argv) == 4:
   path = sys.argv[2]
   filename = sys.argv[3]
print "Downloading %s" % (title)
mp3file = urllib2.urlopen(downloadLink)
with open(os.path.join(path,filename), 'wb') as output:
   output.write(mp3file.read())
print "File Successfully downloaded to : %s\nFilename : %s" % (path,filename)
