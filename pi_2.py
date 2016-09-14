from math import factorial
from math import pi
from decimal import *

getcontext().prec = 10000

def pi_sum(k):
	pi_it = Decimal(( ((-1.)**k) * (factorial(6.*k)) * (545140134.*k+13591409.) ) / ( (factorial(3.*k)) * ( (factorial(k))**3. ) * (640320.**(3.*k + (3./2.))) ))
	return pi_it

def recip_pi(k):
	con = 12
	pipart = 0
	for i in range(k):
		pipart += pi_sum(i)
	pi = 12 * pipart
	return Decimal(pi)
print "My approx:"
print Decimal(1/recip_pi(15))
print "The real pi"
print Decimal(pi)

