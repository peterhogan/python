from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Type a number.")
	
	if how_much < 50:
		print "Modest, you win."
		exit(0)
	else:
		dead("Greedy!")

def bear_room():
	print "There is a bear in the room!"
	print "The bear has a pot of honey."
	print "The bear is in front of another door."
	print "How do you move the bear?"
	bear_moved = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slashes your face")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can now pass."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets angry and eats you.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I have no idea what that is..."


def cthulhu_room():
	print "Here you see the great Cthulhu."
	print "He stares at you and you begin to lose your mind, what do you do?"

	choice = raw_input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Head eaten")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You're in a dark room, there's a door on the left and a door on the right.. which do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You starve.")

start()

