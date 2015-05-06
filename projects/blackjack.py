from random import shuffle
from time import sleep

suits = [u'\u2665',u'\u2663',u'\u2666',u'\u2660'] # These are the unicode suits
ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K'] # These are the card ranks used to build the deck

# The function that deals the cards and also checks there are cards to deal in a given deck
def deal(player, deck):
	if deck == []:
		print "No more cards"
		build(deck1)
		shuffle(deck)
	card = deck[0]
	player.append(deck.pop(0)) # This function deals a card and removes it from the deck
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
	sleep(1)
	print "With value %i." % handval(player)

# builds a deck of cards from the given ranks and suits
def build(deckname):
	for suit in suits:
       		for i in ranks:
                	deckname.append((i,suit)) 
	return deckname

# Determines who wins by who isn't bust and then the highest score
def whowins(you, dealer):
	if bust == True or (bust == False and dealerbust == False and handval(you) < handval(dealer)):
		return "Winner: Dealer"
	elif dealerbust == True or (dealerbust == False and bust == False and handval(dealer) < handval(you)):
		return "Winner: You"
	elif handval(you)==handval(dealer):
		return "Push."

deck1 = []

build(deck1)
shuffle(deck1)

you = []
dealer = []


deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
deal(you, deck1)
print deck1
deal(you, deck1)
print deck1

summary(you, 'You')

deal(you, deck1)
print deck1

summary(you, 'You')
