from time import time
from time import sleep


length = int(input("How long to run the program? "))

counter = 0
now = time()

while time() < now+length:
	counter += 1
	print(counter)
	sleep(1)
