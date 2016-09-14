from lxml import html
from time import sleep
import requests

page = requests.get('https://www.archlinux.org/')
tree = html.fromstring(page.text)

path = '//*[@id="news"]/h4[1]/a' 
content_path = '//*[@id="news"]/div[1]/p[2]'

'//*[@id="news"]/h4[2]/a'
'//*[@id="news"]/div[2]/p[1]'
'//*[@id="news"]/div[2]/p[2]'

news = tree.xpath(path+'/text()')
content = tree.xpath(content_path+'/text()')
#print("#"*50)
for i in range(1,10):
    try:
        print(str(i)+'.',tree.xpath('//*[@id="news"]/h4['+str(i)+']/a/text()')[0])
        print("#"*50)
        #sleep(1)
        for j in range(1,10):
            try:
                print(tree.xpath('//*[@id="news"]/div['+str(i)+']/p['+str(j)+']/text()')[0])
            except IndexError:
                break
        print('#'*50)
        #sleep(0.6)
    except IndexError:
        break
