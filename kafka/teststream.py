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
    pass
else:
    quit('Now exiting, no files downloaded')


#########################################################################
######### Define the main XML parsing/Stream publisher function ######### 
#########################################################################


# function to read the root titles from an already-parsed rss xml file
def RootTitles(read_file):
    try:
        titleout = read_file.xpath('//channel/title')[0].text
    except IndexError:
        titleout = ' '
        # would like some sort of regex title on the filename: titleout = re.search('^[a-zA-Z]+',FILENAME).group(0)
        # but how to get filename?
    return titleout

# function to read the build date from an already-parsed rss xml file - if it exists
def BuildDates(read_file):
    try:
        buildout = read_file.xpath('//channel/lastBuildDate')[0].text
    except IndexError:
        buildout = ' ' 
    return buildout


def PublishArticle(read_file):
    # Get the item title
    print('getting item title')
    try:
        itemtitle = read_file.xpath('//channel/item/title')[i].text
        print(itemtitle)
    except IndexError:
        itemtitle = 'NO ITEM TITLE FOUND'

    # Get the item Description and remove any html tags
    print('getting item desc')
    try:
        itemdescpre = read_file.xpath('//channel/item/description')[i].text
        itemdescsoup = BeautifulSoup(itemdescpre, "lxml")
        itemdesc = itemdescsoup.get_text()
        print(itemdesc)
    except IndexError:
        itemdesc = ' ' 

    # Get Publish Dates
    try:
        itempubdate = read_file.xpath('//channel/item/pubDate')[i].text
    except IndexError:
        itempubdate = ' ' 

    print('forming article:')
    rss_article = print(itemtitle,sep,itemdesc,sep,itempubdate)
    rss_article

    return


###################################
######### Start Streaming ######### 
###################################

# start the kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Open the rssfeeds text file for parsing
with open(rssfeedfile) as feedsources:
    rssfeeds = feedsources.read().splitlines()

# pull out the news sources one by one
for feed in rssfeeds:

    if feed.startswith('http'):
        # download the file by url
        response = urllib.request.urlopen(feed)
        rssfile = etree.parse(response)
        for i in range(len(rssfile.xpath('//channel/item'))):
            # Get the item title
            try:
                itemtitle = rssfile.xpath('//channel/item/title')[i].text
            except IndexError:
                itemtitle = 'NO ITEM TITLE FOUND'

            # Get the item Description and remove any html tags
            try:
                itemdescpre = rssfile.xpath('//channel/item/description')[i].text
                itemdescsoup = BeautifulSoup(itemdescpre, "lxml")
                itemdesc = itemdescsoup.get_text()
            except IndexError:
                itemdesc = ' ' 

            # Get Publish Dates
            try:
                itempubdate = rssfile.xpath('//channel/item/pubDate')[i].text
            except IndexError:
                itempubdate = ' ' 

            rss_article_tuple = (itemtitle,itemdesc,itempubdate)
            rss_article = ' | '.join(rss_article_tuple)
            producer.send('python-test', rss_article.encode('utf-8'))
    else:
        continue
