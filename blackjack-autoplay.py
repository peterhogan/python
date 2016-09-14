from random import shuffle
from time import sleep

#suits = ['H','C','D','S']  # These are the text suits
suits = [u'\u2665',u'\u2663',u'\u2666',u'\u2660'] # These are the unicode suits
ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K'] # These are the card ranks used to build the deck

# The function that deals the cards and also checks there are cards to deal in a given deck
def deal(player, deck):
	print deck
	if deck == []:
		print "No more cards"
		deck = build()
		shuffle(deck)
		print deck
		sleep(3)
	card = deck[0]
	player.append(deck.pop(0)) # This function deals a card and removes it from the deck
	print card
	print deck
	return str(card[0])+card[1]
	#if len(deck) > 0:
	#	card = deck[0]
	#	player.append(deck.pop(0)) # This function deals a card and removes it from the deck
	#elif len(deck) == 0:
	#	print 'Out of cards, reshuffling...'
	#	sleep(0.5)
	#	print '...'
	#	sleep(0.5)
	#	deck = build(deck)
	#	shuffle(deck)
	#	player.append(deck.pop(0)) # This function deals a card and removes it from the deck
	#	card = deck[0]
	#return str(card[0])+card[1]

# This function counts the value of the hand
def handval(hand):
	value = 0
	count_aces = 0
	for i in hand:
		#print "Evaluating card: %r" % i[0]
		#print "Count Aces: %d" % count_aces
		if i[0] == 'A':
			if value + 11 > 21:
				value += 1
			else:
				count_aces += 1
				value += 11

		elif  i[0]=='J' or i[0]=='Q' or i[0]=='K':
			if value + 10>21 and count_aces>0:
				count_aces -= 1
			else:
				value += 10 
		else:
			if value + int(i[0]) > 21 and count_aces>0:
				value += int(i[0])
				value -= 10
				count_aces -= 1
			else:
				value += int(i[0])
		#print "Hand Value: %d" % value
	return value

# Prints a small summary of the cards the player has and their value
def summary(player, name):
	hand = [str(player[i][0])+player[i][1] for i in range(len(player))]
	print "Cards for %s:" % name
	print ', '.join(hand) 
	#sleep(1)
	print "With value %i." % handval(player)

# builds a deck of cards from the given ranks and suits
def build():
	deck = []
	for suit in suits:
       		for i in ranks:
                	deck.append((i,suit)) # build the deck by cycling through the suits and the ranks
	return deck

# Determines who wins by who isn't bust and then the highest score
def whowins(you, dealer):
	if bust == True or (bust == False and dealerbust == False and handval(you) < handval(dealer)):
		print "Winner: Dealer"
	elif dealerbust == True or (dealerbust == False and bust == False and handval(dealer) < handval(you)):
		print "Winner: You"
	elif handval(you)==handval(dealer):
		print "Push."

######################  Start the game! ############################

deck = build()
#deck = []
wallet = 1000
print "you've got $%d in the bank." % wallet


shuffle(deck) # shuffle the deck

again = True

while again == True:

	you = []
	dealer = []

	print 'place your bets ... '
	bet = input('$')
	
	dealersgo = True

	deal(you, deck)
	deal(dealer, deck)
	deal(you, deck)
	deal(dealer, deck)

	summary(you, 'you')
	print ""
	#sleep(1)
	print "Dealer shows, "
	print str(dealer[0][0])+dealer[0][1]
	print ""
	#sleep(1)
	if handval(you) == 21:
		print "Pontoon!!"
		dealersgo = False
		yourgo = False
	else:
		yourgo = True
	bust=False

	while yourgo == True:
		print '------' 
		#prompt = raw_input("Stick (s) or twist (t)? ")
		prompt = 't' # For automatic play
		if prompt == 't':
			print deal(you,deck), "is drawn .. "
			#sleep(1)
			if handval(you) < 22:
				summary(you, 'you')
			else:
				summary(you, 'you')
				print "%i, BUST!" % handval(you)
				bust = True
				yourgo = False
				dealersgo = False
		elif prompt == 's':
			print 'You stick on %i' % handval(you)
			yourgo = False
	#sleep(1)
	summary(dealer, 'dealer')
	dealerbust = False
	#if bust == True:
	#	print "Dealer wins with %i." % handval(dealer)
	#sleep(1)
	while dealersgo == True:
		print "Dealer's turn..."
		#sleep(2)
		if handval(dealer)<17:
			print deal(dealer,deck), 'is drawn .. '
			#sleep(1)
			summary(dealer, 'dealer')	
		elif handval(dealer) > 16 and handval(dealer) <21:
			print "Dealer sticks on %i." % handval(dealer)
			dealersgo = False
		elif handval(dealer) == 21:
			print "Dealer wins!"
			dealersgo = False
		elif handval(dealer)>21:
			print "Dealer bust!"
			dealerbust = True
			dealersgo = False
	#sleep(1)

	whowins(you,dealer)

	# add one point to whoever wins' score or give the winnings to whoever

	#playprompt = raw_input("Play again? (y/n) ")
	playprompt = 'y' # For automatic play
	if playprompt == 'y':
		#shuffleq = raw_input("Shuffle deck? (y/n) ")
		#shuffleq = 'n' # For automatic play
		#if shuffleq == 'y':
		#	shuffle(deck)
		#else:
		#	pass
		again = True
	else:
		again = False
		quit("Bye!")
