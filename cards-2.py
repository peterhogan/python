from random import shuffle
from time import sleep

#suits = ['H','C','D','S']  # These are the text suits
suits = [u'\u2665',u'\u2663',u'\u2666',u'\u2660'] # These are the unicode suits
ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K'] # These are the card ranks used to build the deck

# The function that deals the cards and also checks there are cards to deal in a given deck
def deal(player, deck):
	if deck == []:
		print "No more cards"
		build(deck)
		shuffle(deck)
		print "Rebuilding deck ..."
		sleep(1)
		print "...Done!"
	card = deck[0]
	player.append(deck.pop(0)) # This function deals a card and removes it from the deck
	return str(card[0])+card[1]

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
	sleep(1)
	print "With value %i." % handval(player)

# builds a deck of cards from the given ranks and suits
def build(deckname):
	for suit in suits:
       		for i in ranks:
                	deckname.append((i,suit)) # build the deck by cycling through the suits and the ranks
	return deckname

# Determines who wins by who isn't bust and then the highest score
def whowins(you, dealer):
	if bust == True or (bust == False and dealerbust == False and handval(you) < handval(dealer)):
		return "Winner: Dealer"
	elif dealerbust == True or (dealerbust == False and bust == False and handval(dealer) < handval(you)):
		return "Winner: You"
	elif handval(you)==handval(dealer):
		return "Push."

######################  Start the game! ############################
deck1=[]
build(deck1)
wallet = 1000
#wallet = input("How much have you got? $")
print "you've got $%d in the bank." % wallet


shuffle(deck1) # shuffle the deck

again = True

while again == True:

	you = []
	dealer = []
 	if wallet == 0:
		quit("Out of money!... No loans here")
	print 'place your bets ... '
	bet = input('$')
	while bet > wallet:
		print "Please only bet what you have in your wallet..."
		bet = input('$')
	wallet -= bet
	
	dealersgo = True

	deal(you, deck1)
	deal(dealer, deck1)
	deal(you, deck1)
	deal(dealer, deck1)

	summary(you, 'you')
	print ""
	sleep(1)
	print "Dealer shows, "
	print str(dealer[0][0])+dealer[0][1]
	print ""
	sleep(1)
	if handval(you) == 21:
		print "Pontoon!!"
		wallet += bet*2
		dealersgo = False
		yourgo = False
	else:
		yourgo = True
	bust=False

	while yourgo == True:
		print '------ Wallet: $%d ------' % wallet 
		prompt = raw_input("Stick (s) or twist (t)? ")
		if prompt == 't':
			print deal(you,deck1), "is drawn .. "
			sleep(1)
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
	sleep(1)
	summary(dealer, 'dealer')
	dealerbust = False
	#if bust == True:
	#	print "Dealer wins with %i." % handval(dealer)
	sleep(1)
	while dealersgo == True:
		print "Dealer's turn..."
		sleep(2)
		if handval(dealer)<17:
			print deal(dealer,deck1), 'is drawn .. '
			sleep(1)
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
	sleep(1)

	win = whowins(you,dealer)
	print win

	# add one point to whoever wins' score or give the winnings to whoever
	if win == "Winner: Dealer": 
		print "You lose $%d" % bet
		print "Wallet: $%d" % wallet
	elif win == "Winner: You": 
		print "You win $%d" % bet 
		wallet += 2*bet
		print "Wallet: $%d" % wallet
	elif win == "Push.":
		wallet += bet
		print "Wallet: $%d" % wallet 
	

	playprompt = raw_input("Play again? (y/n) ")
	if playprompt == 'y':
		#shuffleq = raw_input("Shuffle deck? (y/n) ")
		#shuffleq = 'n' 
		#if shuffleq == 'y':
		#	shuffle(deck)
		#else:
		#	pass
		again = True
	else:
		again = False
		print "You took away $%d" % wallet
		quit("Bye!")
