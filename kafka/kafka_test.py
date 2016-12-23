from kafka import KafkaProducer
from lxml import etree
import urllib.request


texttogo = "Disruption as Storm Barbara starts moving across Scotland | Storm Barbara starts crossing Scotland, causing power cuts and school closures and bringing difficult travelling conditions. | Fri, 23 Dec 2016 13:09:31 GMT"

# start the kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('python-test', texttogo.encode('utf-8'))
