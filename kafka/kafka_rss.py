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
verbose = True

# try to filter out by stray HTML tags "<"
filt = False

# descriptions flag
desc_on = True

##################################################
############### Scraping XML files ############### 
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
        if verbose == True and filt == True:
            print(rss_item_titles[i].text,"|",rss_item_descs[i].text.split("<")[0],"|",rss_item_pubdates[i].text,"|",rss_item_guids[i].text,"|",rss_root_title[0].text)#,"|",rss_root_builddate[0].text)
        elif verbose == True and filt == False :
            print(rss_item_titles[i].text,"|",rss_item_descs[i].text,"|",rss_item_pubdates[i].text,"|",rss_item_guids[i].text,"|",rss_root_title[0].text)#,"|"#,rss_root_builddate[0].text)
        elif verbose == False and filt == True:
            print(rss_item_titles[i].text,"|",rss_item_descs[i].text.split("<")[0],"|",rss_item_pubdates[i].text)
        else:
            print(rss_item_titles[i].text,"|",rss_item_descs[i].text,"|",rss_item_pubdates[i].text)
