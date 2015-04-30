print "You are Jack Bauer, you enter a room with two doors. Do you go through door #1, #2 or check your intel?"

door1 = raw_input("> ")

if door1 == '1' or door1 == '#1':
	print "There's a terrorist in here arming a bomb. What do you do?"
	print "1. Point your gun at the terrorist and shout at him."
	print "2. Shoot him in the head."
	
	terrorist = raw_input("> ")
	
	if terrorist == '1':
		print "The terrorist sets off the bomb, you take cover but are caught in the deadly blast. DAMMIT!"
	elif terrorist =='2':
		print "Chloe radios in 'That was our only lead Jack'.. DAMMIT!"
	else:
		print "%s? Jack Bauer would never do that." % terrorist 

elif door1 == '2' or door1 == '#2':
	print "It's a room full of terrorists! What now?"
	print "1. Take cover and call for backup."
	print "2. Pull out your gun and start shooting."
	print "3. Throw a grenade."
	
	room2 = raw_input("> ")
	
	if room2 == '1' or room2 == '3':
		print "Not very Jack Bauer at all... DAMMIT!"
	else:
		print "You kill multiple terrorists until one is left, you haven't sustained a single wound."

else:
	print "It's Chloe, 'Dammit Jack you're wasting time!'"
