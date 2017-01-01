#######################################
############### Imports ############### 
#######################################
import urllib.request
import shutil
import re
import os, errno

############################################
############### Inital setup ############### 
############################################

# Function to read nice byte sizes:
def size_format(x, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(x) < 1024.0:
            return "%3.1f%s%s" % (x, unit, suffix)
        x /= 1024.0
    return "%.1f%s%s" % (x, 'Yi', suffix)

# check the required news feeds directory exists
try:
    os.makedirs('newsfeeds')
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise

# specify the location of the feed file (text file full of rss links)
rssfeedfile = 'rssfeeds.txt'
# check before downloading
cont = input("Do you want to download the RSS files from %s ? (y/n) " % rssfeedfile)
if cont == 'y':
    pass
else:
    quit('Now exiting, no files downloaded')

##################################################
############### Start the Download ############### 
##################################################

# total file size downloaded counter:
total_size = 0

# start an increment to label files
inc = 1

# start the actual download process
with open(rssfeedfile) as feedsources:
    rssfeeds = feedsources.read().splitlines()
for feed in rssfeeds:
    if feed.startswith('http'):
        # specify the filename
        feedoutput_name = 'newsfeeds/' + feed_tag + str(inc) + '.xml'
        # get the file
        print('Downloading',feed,'as',feed_tag + str(inc))
        try:
            site = urllib.request.urlopen(feed)
            meta = site.info()
            feed_file_size = meta.get_all('Content-Length')[0]
            print('Size:',size_format(int(feed_file_size)))
        except TypeError:
            print("Couldn't get file size - no Content-Length given in headers")
        # Add in error code handling here (404 etc.) --->
        with urllib.request.urlopen(feed) as response, open(feedoutput_name, 'wb+') as output_file:
            shutil.copyfileobj(response, output_file)
            total_size += int(os.stat(feedoutput_name).st_size)
        inc+=1
    elif feed.startswith('IGNORE'):
        print('Ignoring feed: %s' % (feed))
    else:
        print('Now downloading feeds from',feed)
        feed_tag=feed[3:].replace(" ","")

# print total files downloaded and size:
print("Downloaded %i files with Total Size: %s" % (inc, size_format(int(total_size))))
