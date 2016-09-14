from glob import glob
from random import sample
from os import system

list_ns = glob('/home/pine/Dropbox/Camera Uploads/*.jpg')
list=[]
for i in list_ns:
	list.append(i.replace(' ','\ '))

for i in sample(list,10):
	print("Copying %s to /static/photos..." % i)
	system('cp %s /home/pine/python/django/mysite2/photos/static/photos/' % i)

