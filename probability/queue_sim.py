from randomdev import randint
from randomdev import randint_gen
from time import time
from time import sleep
from datetime import timedelta
import sys

interval =  0#float(input("Iteration interval (seconds): "))
length = 10#int(input("Run simulation for how many seconds? "))

now = time()
count = 0

server_wait = "0 |"
server_serv = "0x|"

cust = "x"

arrive = randint(0,5)
serve  = randint(6,10)

queue = 0

while time() < now+length:
#	print(server_wait,queue*cust)#, end="\r")
	x = randint(0,1000)

	if x == arrive:
		queue += 1
	else: pass

#	print(server_wait,queue*cust)#, end="\r")

	y = randint(1,1000)

	if y == serve:
		queue -= 1
	else: pass

	print("%s%r" % (server_wait,queue*cust), end='\r', flush=True)

	sleep(interval)









