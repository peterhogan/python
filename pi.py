from decimal import *
from math import sqrt
from math import pi
from math import factorial as fac

### How precise would you like to be?

#precis = input("How many decimal places to show? ")
precis = 100

getcontext().prec = precis

### Fibonacci Test ###

#fib_howmany = input("How many terms of the fibonacci sequence would you like? ") - 2
fib = [1,1]
#for i in range(fib_howmany):
#	fib.append(fib[-1]+fib[-2])

#fib_print_question = raw_input("Print them? (y/n) ")

#if fib_print_question == 'y':
#	for i in fib:
#		if i == fib[-1]:
#			print "%d." % i,
#		else:
#			print "%d,"% i,

###

# a_n+1 = a_n+b_n/2
# b_n+1 = sqrt(a_n b_n)
# t_n+1 = t_n - p_n(a_n - a_n+1)^2
# p_n+1 = 2p_n
#
# pi_approx = (a_n+1 + b_n+1)^2 / 4*t_n+1

a = [1.]
b = [1/sqrt(2)]
t = [1./4]
p = [1.]

pi_approx = []

for i in range(1000):
	an = (a[-1]+b[-1])/2
	bn = sqrt(a[-1]*b[-1])
	tn = t[-1]-p[-1]*(a[-1]-an)**2
	pn = 2*p[-1]

	a.append(an)
	b.append(bn)
	t.append(tn)
	p.append(pn)

	pi_appn = ((an + bn)**2)/(4*tn)

	pi_approx.append(pi_appn)


print "Trying to approximate 3.141592653589793238462643383279502884197169399375105820974944592307816406286"



###### 2nd attempt ####


def pisum(n):
	sum_term = ((-1)**n)/(2**(10*n))*(-(2**5)/(4*n+1)-(1/(4*n+3))+((2**8)/(10*n+1))-((2**6)/(10*n+3))-((2**2)/(10*n+5))-((2**2)/(10*n+7))+(1/(10*n+9)))
	return sum_term

const = 1/(2**6)
top = 200

sumpi = 0

for i in range(0,top):
	const*pisum(i),

##### 3rd Attempt ######

def pi_sum_term(k):
	return (((-1.)**k)*fac(6.*k)*(545140134.*k+13591409.))/(fac(3.*k)*(fac(k)**3.)*(640320.**(3.*k+(3./2)))
