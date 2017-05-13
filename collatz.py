from time import sleep

def collatz():
	entry = input("Please enter an integer: ")
	steps = 0
	while entry != 1:
		if entry % 2 == 0:
			entry = entry/2
		else:
			entry = (entry*3)+1
		steps += 1
		print(entry)
	print("Done! In %d steps." % steps)

def collatz_iter(limit):
	for i in range(2,limit+1):
		j = i
		steps = 0
		while i != 1:
			if i % 2 == 0:
				i = i/2
			else:
				i = (i*3)+1
			steps += 1
		print("%d took %d steps" % (j, steps))
def coll_supp(n):
	steps = 0
	while n != 1:
		if n % 2 == 0:
			n = n/2
		else:
			n = (n*3)+1
		steps += 1
	return steps

again = 'y'

#while again == 'y':
#	collatz()
#	again = raw_input("again? .. (y/n)")


i=2
while 0!=1:
	print("%d took %d steps." %(i, coll_supp(i)))
	i += 1
	#sleep(0.1)	

	


