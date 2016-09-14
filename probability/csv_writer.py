import csv
import sys
from randomdev import randint
from time import clock
from random import gammavariate as gamma

f = open(sys.argv[1], 'wt')

try:
	writer = csv.writer(f)
	writer.writerow( ('index','gamma') )
	for i in range(1000):
		writer.writerow( ((i+1), gamma(4,5)) )
finally:
	f.close()

print(open(sys.argv[1], 'rt').read())
