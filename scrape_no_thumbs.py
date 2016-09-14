import fnmatch
import os

matches = []
for root, dirnames, filenames in os.walk('/home/pine/python/django/mysite2/'):
	if fnmatch.fnmatch(root,'*/thumbnails'):
		break
	for filename in fnmatch.filter(filenames, '*.jpg'):
		matches.append(os.path.join(root, filename))
print(matches)
