from bs4 import BeautifulSoup
import urllib
import os
from random import randint
from time import sleep
import re
	
# Get page and use BeautifulSoup to make into a tree thing or something?
page = urllib.urlopen('http://themmpodcast.com/audio/').read()
soup = BeautifulSoup(page, "lxml")

# Look for all the anchor tags that have a href attribute ending in .mp3.
download = soup.find_all('a', href = re.compile('\.mp3$'))
for anchor in download:
	hrefText = (anchor['href'])
	exists = anchor.text# Used to see if we already downloaded this podcast.

	if (os.path.isfile(exists)):# os.path.isfile() returns true if the file already exists.
		print "%s has already been downloaded. Skipping to next one." % exists

	else:
		print "Currently downloading: %s\n\n" % hrefText
        os.system('wget http://themmpodcast.com/audio/%s' % hrefText)# Download the .mp3 with wget.
	
		# Use this section if you think you are having issues downloading.
		# This code will make the script pause after every download for a random amount of time
		# between 60 and 180 seconds.  This may or may not help.
		#number = randint(60, 180)
		#print "Sleeping for %d seconds so we don't get blocked by the server." % number
		#sleep(number)

		# Format Output
		for i in range(0, 10):
			print "\n"
# Format Output
for i in range(0, 10):
	print "\n"
print "\tAll of the MMPodcasts posted to themmpodcast.com/audio/ should be downloaded."
print "\tHowever, running this script again will download all the .mp3's again."
print "\tThis script will not check for duplicates.  Also no new podcasts are posted"
print "\there so you don't have to worry about running it again anyway.  Just make"
print "\tyou got all of them properly from here.  Maybe try the script twice.\n\n\n"
