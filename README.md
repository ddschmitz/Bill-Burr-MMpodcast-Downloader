# Bill-Burr-MMpodcast-Downloader

Two programs to download all of the Monday Morning Podcasts from [themmpodcast.com](http://themmpodcast.com/audio/) and [libsyn](http://billburr.libsyn.com/).  Themmpodcast.com contains older ones and I don't think has new ones added to it so you just need to run that program once.  Libsyn however is updated as new podcasts come out so if you want the new ones all you have to do is run the libsyn program again (It will skip over ones you currently have).  

### Running the programs.

These two programs were written with Python 2.7 and require you to have Beautiful Soup installed.  They also use `wget` to download the podcasts so it would be best to run these in a Linux environment.  All programs will be downloaded to the same directory that the .py file is in.

##### Install [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup).

`sudo apt-get install python-bs4`

##### Running.

`python MMPlibsyn.py`

and

`python MMPthemmpodcast.py`

### If You Encounter Troubles.

Sometimes I encounter troubles with the downloading of the podcasts.  Sometimes `wget` would say something like "connection reset by peer".  I came up with two ways to possibly get around this.

##### Using [torsocks](https://github.com/dgoulet/torsocks).

`sudo apt-get install tor`

`sudo service tor start`

`torsocks python MMPlibsyn.py`

`torsocks python MMPthemmpodcast.py`

##### Delay after each download.

There are three lines in both scripts that you can uncomment to pause the program for a random amount of time after each download.  This trick seemed to work sometimes but I wouldn't guarantee that this will allow the program to run free of interuptions.  I would highly recommend trying to use torsocks first.  

Uncomment these three lines:

```python
number = randint(60, 180)
print "Sleeping for %d seconds so we don't get blocked by the server." % number
sleep(number)
```
