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

# verbose output or brief (True => Verbose, False => short output)
verbose = False

##################################################
###############                    ############### 
##################################################

for filerss in os.listdir(root_dir):
    rss_file = etree.parse(root_dir + filerss)

    rss_root_title = rss_file.xpath('//channel/title')
    rss_root_builddate = rss_file.xpath('//channel/lastBuildDate')
    rss_item_titles = rss_file.xpath('//channel/item/title')
    rss_item_descs = rss_file.xpath('//channel/item/description')
    rss_item_pubdates = rss_file.xpath('//channel/item/pubDate')
    rss_item_guids = rss_file.xpath('//channel/item/guid')

    for i in range(len(rss_item_titles)):
        if verbose == True:
            print(rss_item_titles[i].text,"|",rss_item_descs[i].text,"|",rss_item_pubdates[i].text,"|",rss_item_guids[i].text,"|",rss_root_title.text,"|",rss_root_builddate.text)
        else:
            print(rss_item_titles[i].text,"|",rss_item_descs[i].text,"|",rss_item_pubdates[i].text)
