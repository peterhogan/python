#######################################
############### Imports ############### 
#######################################
from lxml import etree
import os

############################################
############### Inital setup ############### 
############################################

# specify the directory to pull feeds from (default from get_rss_feeds.py)
root_dir = 'newsfeeds/'

# verbose output or brief (default verbose)
verbose = True

##################################################
###############                    ############### 
##################################################

for file in os.path(root_dir):
    rss_file = etree.parse(file)

    rss_root_title = rss_file.xpath('//channel/title')
    rss_root_builddate = rss_file.xpath('//channel/lastBuildDate')
    rss_item_titles = rss_file.xpath('//channel/item/title')
    rss_item_descs = bbc_rss.xpath('//channel/item/description')
    rss_item_pubdates = bbc_rss.xpath('//channel/item/pubDate')
    rss_item_guids = bbc_rss.xpath('//channel/item/guid')

    for i in range(len(rss_item_titles)):
        if verbose == True:
            print(rss_item_titles[i].text,"|",rss_item_descs[i].text,"|",rss_item_pubdates[i].text,"|",rss_item_guids[i].text,"|",rss_root_title[i].text,"|",rss_root_builddate[i].text)
        else:
            print(rss_item_titles[i].text,"|",rss_item_descs[i].text,"|",rss_item_pubdates[i].text)
