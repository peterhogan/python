from lxml import html
import requests

page = requests.get('http://www.bbc.co.uk/news')
tree = html.fromstring(page.text)

#//*[@id="comp-candy-asset-munger"]/div/div[1]/div/div[2]/a/h3/span
#//*[@id="comp-pattern-library"]/div/div/a[1]/h3/span

headlines = tree.xpath('//*[@id="comp-candy-asset-munger"]/div/div[1]/div/div[2]/a/h3/span')

for i in headlines:
    print(i)
