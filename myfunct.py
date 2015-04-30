print "First give me a numerator: ",

num = float(raw_input("... "))

print "Now give me a denominator: ",

denom = float(raw_input("... "))

def number(numerator, denominator):
	print "The numerator is %d." % numerator 
	print "The denominator is %d." % denominator
	print "As a fraction we have %d/%d." % (numerator, denominator)
	deci = float(numerator/denominator)
	print "As a decimal we have %f." % deci 


print number(num, denom)
