from randomdev import randint
from randomdev import randint_gen
from time import time
from time import sleep
from datetime import timedelta

#supress = input("Run in quiet mode (y/n)? ")

interval = float(input("Iteration interval (seconds): "))

length = int(input("Run simulation for how many seconds? "))

#birth_prob = float(input("
now = time()
count = 0

birthtarget = randint(0,5)
deathtarget = randint(6,10)

population = 150

while time() < now+length:
	print("Population:", population, "at time:",time(),end="\r")
	x = randint(0,1000)

	if x == birthtarget:
		population += 1
	else: pass

	print("Population:", population, "at time:",time(),end="\r")

	y = randint(1,500)

	if y == deathtarget:
		population -= 1
	else: pass

	print("Population:", population, "at time:",time(),end="\r")

	sleep(interval)

print("Population reached", population,"in",length,"seconds.")
print("That's a change of",population-150)







