from lxml import etree
import urllib.request
import shutil

url = "http://feeds.bbci.co.uk/news/rss.xml?edition=int"
#url = "http://feeds.bbci.co.uk/news/video_and_audio/technology/rss.xml"

with urllib.request.urlopen(url) as response, open('bbc_rss1.xml', 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')

bbc_rss = etree.parse('bbc_rss1.xml')
#bbc_rss = etree.parse(out_file)

bbc_titles = bbc_rss.xpath('//channel/item/title')
bbc_desc = bbc_rss.xpath('//channel/item/description')
bbc_date = bbc_rss.xpath('//channel/item/pubDate')

for i in range(len(bbc_titles)):
    print("#############")
    print(bbc_titles[i].text,"|",bbc_desc[i].text,"|",bbc_date[i].text)
