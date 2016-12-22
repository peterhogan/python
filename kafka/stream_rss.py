#######################################
############### Imports ############### 
#######################################
from kafka import KafkaProducer
import urllib.request
import shutil
import re
import os, errno

'''
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
'''

text_to_send = ''' <?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet title="XSL_formatting" type="text/xsl" href="/shared/bsp/xsl/rss/nolsol.xsl"?>
<rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom" version="2.0" xmlns:media="http://search.yahoo.com/mrss/">
    <channel>
            <title><![CDATA[BBC News - Home]]></title>
                    <description><![CDATA[BBC News - Home]]></description>
                            <link>http://www.bbc.co.uk/news/</link>
                                    <image>
                                                <url>http://news.bbcimg.co.uk/nol/shared/img/bbc_news_120x60.gif</url>
                                                            <title>BBC News - Home</title>
                                                                        <link>http://www.bbc.co.uk/news/</link>
                                                                                </image>
                                                                                        <generator>RSS for Node</generator>
                                                                                                <lastBuildDate>Thu, 22 Dec 2016 21:10:29 GMT</lastBuildDate>
                                                                                                        <copyright><![CDATA[Copyright: (C) British Broadcasting Corporation, see http://news.bbc.co.uk/2/hi/help/rss/4498287.stm for terms and conditions of reuse.]]></copyright>
                                                                                                                <language><![CDATA[en-gb]]></language>
                                                                                                                        <ttl>15</ttl>
                                                                                                                                <item>
                                                                                                                                '''

###################################
######### Start Streaming ######### 
###################################

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('python-test', text_to_send.encode('utf-8'))
