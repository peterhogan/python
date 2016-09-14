from scipy.integrate import quad

def integrand(t,n,x):
	return exp(-x*t)/t**n

def expint(n,x):
	return quad(integrand, 0, Inf, args(n,x))[0]

print(expint(2,1.0))
