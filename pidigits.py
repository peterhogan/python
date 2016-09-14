from math import factorial
from math import pi
from decimal import *

def pisum(n):
        sum_term = ((-1)**n)/(2**(10*n))*(-(2**5)/(4*n+1)-(1/(4*n+3))+((2**8)/(10*n+1))-((2**6)/(10*n+3))-((2**2)/(10*n+5))-((2**2)/(10*n+7))+(1/(10*n+9)))
        return sum_term

const = 1/(2**6)


print pisum(0)


def pi_nth_term(n):
	term =Decimal( ( ( (factorial(n))**2. ) * (2.**(n+1.))  )/(factorial(2.*n + 1.)))
	return term

pi_me = Decimal(0.)
for i in range(89):
	pi_me +=  pi_nth_term(i)

print Decimal(pi_me)

print Decimal(pi)
