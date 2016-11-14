from lxml import html
from time import sleep
import requests

page = requests.get('http://www.bbc.co.uk/news')
tree = html.fromstring(page.text)

#//*[@id="comp-pattern-library"]/div/div/a[1]/h3/span
path4 = '//*[@id="comp-candy-asset-munger"]/div/div[2]/div/div[2]/a/h3/span'
path5 = '//*[@id="comp-pattern-library"]/div/div/div[2]' 
path6 = '//*[@id="comp-candy-asset-munger"]/div/div[1]/div/a/h3/span'

headline = tree.xpath('//*[@id="comp-pattern-library"]/div/div/a[1]/h3/span/text()')
headline2 = tree.xpath('//*[@id="comp-candy-asset-munger"]/div/div[1]/div/div[2]/a/h3/span/text()')
headline3 = tree.xpath('//*[@id="comp-candy-asset-munger"]/div/div[3]/div[1]/a[1]/h3/span'+'/text()')
headline4 = tree.xpath(path4+'/text()')
headline5 = tree.xpath(path5+'/text()')
headline6 = tree.xpath(path6+'/text()')

headers = [headline2,headline3,headline4,headline6]


#print('Headline: ', headline[0])
sleep(1)
for heads in headers:
    for article in heads:
        sleep(0.3)
        print(article)
