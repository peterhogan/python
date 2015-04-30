def cheese_and_crackers(cheese_count, cracker_count):
	print "You have %d packets of cheese." % cheese_count
	print "You have %d boxes of crackers!" % cracker_count
	print "That's enough for a party,"
	print "Get a blanket.\n"

print "we can give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"
amnt_cheese = 10
amnt_crackers = 40

cheese_and_crackers(amnt_cheese,amnt_crackers)

print "We can even do maths in the function:"
cheese_and_crackers(10+20,27 % 9)

print "And finally combine the two"
cheese_and_crackers(amnt_cheese+1,amnt_crackers+1)
