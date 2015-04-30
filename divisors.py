#This function lists an arithmetic sequence between two values with a given increment 
def list_nos(start,end,incr):
        i=start
        numbers=[]
        while i<end:
                numbers.append(i)
                i+=incr
        return numbers

#This function tells you if a number is a divisor of a chosen number
def divi(num,div): #we want to know if div is a divisor of num
	result = int(num)%int(div)
	if result == 0:
		print "Divisor"
	else:
		print "Not a divisor"

#This function gives you the divisors of a number
def divisor(number):
	numbers=range(1,number+1)
	divisors=[]
	for i in numbers:
		if number%i == 0:
			divisors.append(i)	
		else:
			pass
	return divisors
 	
#This next function gives you the primes between 1 and your number
def prime_nos(number):
	primes =[]
	for n in range(2,number+1):
		for x in range(2,n):
			if n % x == 0:
				pass
				break
		else:
			primes.append(n)		
	return primes

#This function gives the set intersection of two lists
def intersect(a,b):
	return list(set(a) & set(b))

x = int(raw_input("Type a number to show its divisors and prime factors "))
print "The divisors of", x, "are:", divisor(x)
print "The prime factors are: ", intersect(divisor(x),prime_nos(x))
