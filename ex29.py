people = int(raw_input("How many people are there? "))
cats = int(raw_input("How many cats are there? "))
dogs = int(raw_input("How many dogs are there? "))

if people < cats:
	print "Too many cats!"

if cats < people:
	print "Too many people!"

if people < dogs:
	print "Too many dogs!"

if dogs < people:
	print "Too many people!"

if people > cats and people > dogs:
	print "People everywhere!!"

dogs += 5

if people >= dogs:
	print "There's more or equal people than dogs."

if dogs >= people:
	print "There's more or equal dogs than people."

if people == dogs:
	print "People are dogs!" 
