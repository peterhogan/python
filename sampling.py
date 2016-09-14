import random
import csv
from time import sleep

random.seed(23102012)

population1 = []
seq = range(1,1000)
random.shuffle(seq)

for i in range(1,1000):
	n = 100*round(random.random(),3)
	population1.append(n)

for i in range(1,50):
	#print seq[i]
	print population1[i]
	sleep(1)
	

