import logging

logging.basicConfig(filename='test-logfile.log', level=logging.DEBUG)

top = 50

for i in range(top):
	print(i)
logging.info('Loop completed, reached %s' % top)
