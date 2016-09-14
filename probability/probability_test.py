from randomdev import randint
from randomdev import randint_gen
from time import clock
from time import sleep

x = 0
start = clock()
while x != 1:
	x = randint(0,100)/100
	print(x)
	#sleep(0.3)

print("Done in", clock() - start, "seconds.")
