def add(a, b):
	print "adding %d + %d" % (a,b)
	return a+b

def subtract(a,b):
	print "subtracting %d - %d" % (a,b)
	return a-b

def times(a,b):
	print "multiplying %d by %d" % (a,b)
	return a*b

def div(a,b):
	print "dividing %d by %d" % (a,b)
	return a/b

print "Let's do some maths!"

age = add(20,3)
height = subtract(100,40)
weight = times(2,4)
iq = div(100,2)

print "Age: %d, Height %d, Weight: %d, IQ: %d" % (age,height,weight,iq)
