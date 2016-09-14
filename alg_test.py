from random import randint 
from math import sqrt
from time import clock
from time import time

#a = randint(10000,10000000)
#b = randint(10000,10000000)

#print "(%d, %d)" % (a,b)

estimates = []
def estimate():
	if len(estimates) != 0:
		return float(sum(estimates))/len(estimates)

guess = 0
itr_length = 0
primes = []
n = 1 # input("pick a number ")
i = 2
start_time = clock()
while i < n:
	start = clock()
	perc = round((float(i)/n)*100, 2)
	print perc,"% done...", guess,"seconds remaining         \r",
	for j in range(2,i):
		if i % j == 0:
			break
	else:
		primes.append(i)
	end = clock()
	itr_length = end-start
	estimates.append(itr_length)
	guess =round(estimate()*(n-i),2)
	i += 1

end_time = clock()
timetaken = end_time - start_time

print "There are",len(primes),"prime numbers less than", n
print timetaken, "seconds taken"

# Alg 2 for checking primes

#p = 2
#primes = [p]
#p += 1
#primes.append(p)
#max = input("List primes up to ... ? ")
#while p < int(max):
#	p += 2
#	test = True
#	sqrtp = sqrt(p)
#	for i in primes:
#		if i>sqrtp: break
#		if p%i==0:
#			test=False
#			break
#		if test and p not in primes: primes.append(p)
#	
#print "There are ",len(primes),"primes less than", max,


guess = 0
itr_length = 0
primes = [2]
n = 1 # input("pick a number ")
i = 3
start_time = clock()
while i < n:
	start = clock()
	perc = round((float(i)/n)*100, 2)
	print perc,"% done...", guess,"seconds remaining         \r",
	for j in primes:
		if i % j == 0:
			break
	else:
		primes.append(i)
	end = clock()
	itr_length = end-start
	estimates.append(itr_length)
	guess =round(estimate()*(n-i),2)
	i += 2

end_time = clock()
timetaken = end_time - start_time

print "There are",len(primes),"prime numbers less than", n
print timetaken, "seconds taken"


def gcd(a,b):
	while b != 0:
		t = b
		b = a % b
		a = t
	return a

def brent(N):
	if N%2==0:
		 return 2
	y,c,m = randint(1, N-1),randint(1, N-1),randint(1, N-1)
	g,r,q = 1,1,1
	while g==1:             
		x = y
                for i in range(r):
                        y = ((y*y)%N+c)%N
                k = 0
                while (k<r and g==1):
                        ys = y
                        for i in range(min(m,r-k)):
                                y = ((y*y)%N+c)%N
                                q = q*(abs(x-y))%N
                        g = gcd(q,N)
                        k = k + m
                r = r*2
        if g==N:
                while True:
                        ys = ((ys*ys)%N+c)%N
                        g = gcd(abs(x-ys),N)
                        if g>1:
                                break
         
        return g

def listprod(input):
	i=0
	while i != len(input):
		input[i]*input[i+1]
		i += 2	
	
hat = [1,2,3,4,5,6,7,8,9,10]

print listprod(hat)


n = input("Enter a number to factorise: ")
factors_n = []
while n != brent(n):
	#print n 
	n = n/brent(n)
	print n 
	factors_n.append(n)

factors_n.append(n)

print factors_n




