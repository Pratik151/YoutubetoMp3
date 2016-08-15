import urllib2
import os
import pwd
import json
import sys

def getDetails():
   urlLink = 'http://www.youtubeinmp3.com/fetch/?format=JSON&video=' + sys.argv[1]
   downloadLink = data['link']
   title = data['title']
   path = os.path.join('/home',pwd.getpwuid(os.getuid()).pw_name,'Music')
response = urllib2.urlopen(urlLink)
data = json.load(response)
print "Downloading %s" % (title)
mp3file = urllib2.urlopen(downloadLink)

with open(os.path.join(path,'Song.mp3'), 'wb') as output:
   output.write(mp3file.read())
print "File Successfully downloaded to : %s" % (os.path.join(path, 'Song.mp3'))

