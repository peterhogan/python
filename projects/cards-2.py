from random import shuffle
from time import sleep

#suits = ['H','C','D','S']  # These are the suits - these can be made into unicode suits later
suits = [u'\u2665',u'\u2663',u'\u2666',u'\u2660']
ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K'] # These are the ranks that will probably need to be translated into numbers to add up values (partic ace)

#print ranks[0], ranks[-1], ranks[-2], ranks[-3]

def deal(player):
	if len(deck) > 0:
		card = deck[0]
		player.append(deck.pop(0)) # This function deals a card and removes it from the deck
		return str(card[0])+card[1]
	else:
		print 'Out of cards, reshuffling...'
		sleep(0.5)
		print '...'
		sleep(0.5)
		build()
		shuffle(deck)
		card = deck[0]
		player.append(deck.pop(0)) # This function deals a card and removes it from the deck
		return str(card[0])+card[1]


def handval(hand):
	value = 0
	count_aces = [hand[i][0] for i in range(len(hand))].count('A')
	for i in hand:
		if i[0] == 'A':
			if value + 11 > 21:
				value += 1
			else:
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
	return value

def summary(player, name):
	hand = [str(player[i][0])+player[i][1] for i in range(len(player))]
	print "Cards for %s:" % name
	print ', '.join(hand) 
	sleep(1)
	print "With value %i." % handval(player)

def build():
	deck = []
	for suit in suits:
       		for i in ranks:
                	deck.append((i,suit)) # build the deck by cycling through the suits and the ranks
	return deck

def whowins(you, dealer):
	if bust == True or (bust == False and dealerbust == False and handval(you) < handval(dealer)):
		print "Winner: Dealer"
	elif dealerbust == True or (dealerbust == False and bust == False and handval(dealer) < handval(you)):
		print "Winner: You"
	elif handval(you)==handval(dealer):
		print "Push."
deck = build()
wallet = 0

shuffle(deck) # shuffle the deck

again = True

while again == True:

	you = []
	dealer = []

	dealersgo = True

	deal(you)
	deal(dealer)
	deal(you)
	deal(dealer)

	summary(you, 'you')
	print ""
	sleep(1)
	print "Dealer shows, "
	print str(dealer[0][0])+dealer[0][1]
	print ""
	sleep(1)
	if handval(you) == 21:
		print "Pontoon!!"
		dealersgo = False
		yourgo = False
	else:
		yourgo = True
	bust=False

	while yourgo == True:
		print '------' 
		prompt = raw_input("Stick (s) or twist (t)? ")
		if prompt == 't':
			print deal(you), "is drawn .. "
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
			print deal(dealer), 'is drawn .. '
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

	whowins(you,dealer)

	# add one point to whoever wins' score or give the winnings to whoever

	playprompt = raw_input("Play again? (y/n) ")
	if playprompt == 'y':
		shuffleq = raw_input("Shuffle deck? (y/n) ")
		if shuffleq == 'y':
			shuffle(deck)
		else:
			pass
		again = True
	else:
		again = False
		quit("Bye!")



class Player:

	bust = False

	def __init__(self):
		pass

	def deal(player):
		player.append(deck.pop(0))	
	

