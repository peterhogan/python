#i=0
#numbers=[]
#while i<8:
#	numbers.append(i)
#	i += 1
#	print numbers

#for i in numbers:
#	print i

def list_nos(start,end,incr):
	i=start
	numbers=[]
	while i<end:
		numbers.append(i)
		i+=incr
	return numbers

#print list_nos(0,7,1)
