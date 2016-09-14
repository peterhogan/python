from functools import reduce

def factorial(x):
	try:
		result = reduce(lambda i, j: i*j, range(1,x+1))
		return result
	except (RuntimeError, TypeError, NameError):
		return 0
def gamma(x):
	return factorial(x-1)

