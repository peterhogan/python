a = input("Enter the first number ")
b = input("Enter the second number ")

x = max([a,b])
y = min([a,b])

if x%y == 0:
	print "The GCD of %d and %d is %d." % (x,y,y)

	d = x/y
	d = x/y
	r = x-((x/y)*y)
	print "%d = %d * %d + %d" % (x,y, x/y, r)



