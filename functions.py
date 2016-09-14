import random

def randlist(low, high, n):
	list_randlist = []
	for i in range(n):
		x = random.randint(low, high) 
		list_randlist.append(x)	
	print list_randlist


new1 = randlist(0,1,100)
new2 = randlist(0,10,10)
new3 = randlist(-10,10,5)

print new1, new2, new3

