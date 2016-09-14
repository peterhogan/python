import random

def randlist(low, high, n):
	list_randlist = []
	for i in range(n):
		x = random.randint(low, high) 
		list_randlist.append(x)	
	return list_randlist

def count_in_list(list):
	top = max(list)
	bottom = min(list)
	for i in range(bottom, top+1):
	 	n = list.count(i)
		if n != 0:
			print 'There are %d of the number %d in the list' % (n,i)
def mean(list):
	list_length = len(list) # gets the divisor
	list_sum = sum(list) # gets the sum of all the values in the set
	the_mean = float(list_sum)/list_length # calculates the mean
	return the_mean # returns the mean value

def modeprinted(list):
	values = {}
	modes = []
	for i in range(min(list),max(list)+1):
		n = list.count(i)
		if n != 0:
			values[i]=n
	for i in values:
		if values[i] == max(values.values()):
			modes.append(i)
	if len(modes) == 1:
		print "The mode is:", modes[0]
	else:
		print "The modes are:", ', '.join(str(i) for i in modes)

def modevalues(list):
	values = {}
	modes = []
	for i in range(min(list),max(list)+1):
		n = list.count(i)
		if n != 0:
			values[i]=n
	for i in values:
		if values[i] == max(values.values()):
			modes.append(i)
	return modes

def median(list):
	sortedlist = sorted(list)
	length = len(list)
	half_point_trunc = length/2
	one_less_half = half_point_trunc - 1
	if length % 2 == 0:
		avg_even = float(sortedlist[half_point_trunc] + sortedlist[one_less_half])/2
		return avg_even 
	else:
		return sortedlist[half_point_trunc] 

#def splitquarts(list):
	
	
