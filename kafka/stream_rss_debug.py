#######################################
############### Imports ############### 
#######################################
from kafka import KafkaProducer
from lxml import etree
import urllib.request
import shutil
import re
import os, errno

from kfk_rss_read import *

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

# specify the location of the global GUID file
globalGUID = 'globalGUID.log'

# check before streaming
cont = input("Start streaming %s? (y/n) " % rssfeedfile)
if cont == 'y':
    print('Now initiating stream script')
    pass
else:
    quit('Now exiting, no files downloaded')


#########################################################################
######### Define the main XML parsing/Stream publisher function ######### 
#########################################################################


# function to read the root titles from an already-parsed rss xml file
def RootTitles(read_file):
    print('getting root title')
    try:
        titleout = read_file.xpath('//channel/title')[0].text
    except IndexError:
        print('no root title')
        titleout = ' '
        # would like some sort of regex title on the filename: titleout = re.search('^[a-zA-Z]+',FILENAME).group(0)
        # but how to get filename?
    return titleout

# function to read the build date from an already-parsed rss xml file - if it exists
def BuildDates(read_file):
    print('getting build date')
    try:
        buildout = read_file.xpath('//channel/lastBuildDate')[0].text
    except IndexError:
        print('no build date given')
        buildout = ' ' 
    return buildout


def PublishArticles(read_file, masterGUIDFile, kafka_producer, kafka_topic):

    # define the sepatator for the output:
    sep = '|'
    print('separator is',sep)

    # read from the master GUID file to prevent duplicate articles
    guidlist = masterGUIDFile
    print('GUID list is:',guidlist)

    for i in range(len(read_file.xpath('//channel/item'))):
        # Get GUID and pass iteration if it already exists
        try:
            itemguid = read_file.xpath('//channel/item/guid')[i].text
            print('got guid as:',itemguid)
        except IndexError:
            itemguid = read_file.xpath('//channel/item/title')[i].text
            print('no guid found, using title:',itemguid)
        if itemguid in guidlist:
            print('guid found in list, skipping..')
            continue
        else:
            print('unique guid:',itemguid,'adding to guidlist')
            guidlist.append(itemguid)

        # Get the item title
        try:
            itemtitle = read_file.xpath('//channel/item/title')[i].text
            print('item title:',itemtitle)
        except IndexError:
            itemtitle = 'NO ITEM TITLE FOUND'
            print('item title:',itemtitle)

        # Get the item Description and remove any html tags
        try:
            itemdescpre = read_file.xpath('//channel/item/description')[i].text
            itemdescsoup = BeautifulSoup(itemdescpre, "lxml")
            itemdesc = itemdescsoup.get_text()
        except IndexError:
            itemdesc = ' ' 

        # Get Publish Dates
        try:
            itempubdate = read_file.xpath('//channel/item/pubDate')[i].text
        except IndexError:
            itempubdate = ' ' 

        # get root title with separate function
        itemroottitle = RootTitles(read_file)

        # get build date with separate function (if possible)
        itemrootdate = BuildDates(read_file)

        rss_article = itemtitle,sep,itemdesc,sep,itempubdate,sep,itemguid,sep,itemroottitle,sep,itemrootdate
        print('created article list as:', rss_article)

        print('now publishing with kafka')
        kafka_producer.send(kafka_topic, rss_article.encode('utf-8'))
        print('published')

    # Flatten GUID file to prevent duplicates being missed through nested lists
    print('Flatten GUID file to prevent duplicates being missed through nested lists')
    guidlist = list(chain(*guidlist))
    print('Done')
    return


###################################
######### Start Streaming ######### 
###################################

# start the kafka producer
print('starting kafka producer: localhost:9092')
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Open the rssfeeds text file for parsing
print('Open the rssfeeds text file for parsing')
with open(rssfeedfile) as feedsources:
    rssfeeds = feedsources.read().splitlines()

# pull out the news sources one by one
for feed in rssfeeds:

    # add in counters to publish when finished

    if feed.startswith('http'):
        # specify the filename
        feedoutput_name = 'newsfeeds/' + feed
        print(feedoutput_name)
        # download the file by url
        try:
            with urllib.request.urlopen(feed) as response:
                rssfile = etree.parse(response)
                PublishArticles(rssfile, masterGUIDFile = globalGUID, kafka_producer = producer, kafka_topic = 'python-test')
        except: # need all urllib error types here
            continue
    else:
        continue
