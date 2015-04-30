def mod_add(a,b,c):
	print "we will add %s and %s modulo %s" % (a,b,c)
	return (a+b)%c

def mod_sub(a,b,c):
	print "we will subtract %d from %d modulo %d" % (a,b,c)
	return (a-b)%c

print "Let's do some modular arithmetic!"
mod = int(raw_input("What modulus would you like to work with? "))
print "Give me some numbers to add:"
num1 = int(raw_input("First number:...? "))
num2 = int(raw_input("Second number:...? "))
result1 = mod_add(num1,num2,mod)
print "The answer is %d" % result1

print "Now let's subtract, give me some more numbers:"
num3 = int(raw_input("Number one... "))
num4 = int(raw_input("Number two... "))
result2 = mod_sub(num3,num4,mod)
print "The answer is %d" % result2
