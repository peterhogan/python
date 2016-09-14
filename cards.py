from random import shuffle

suits = [u'\u2665',u'\u2663',u'\u2666',u'\u2660']
#suits = ['H','C','D','S']
ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = []

for suit in suits:
	for i in ranks:
		deck.append((i,suit))

cards_print = [deck[i][0]+deck[i][1] for i in range(52)]

#print ' '.join(cards_print)


#print "Now shuffle..."
shuffle(deck)

hand = deck[0:2] 
hand_length = len(hand)
print "Deal a hand of %d cards..." % (hand_length)
print_hand = []

for i in range(hand_length):
	print_hand.append(hand[i][0]+hand[i][1])
print 'Your hand:'
print ' '.join(print_hand)

dealer = deck[2:4]
deal_length = len(dealer)
dealer_print = []
for i in range(deal_length):
	dealer_print.append(dealer[i][0]+dealer[i][1])
print "Dealer's Hand:"
print ' '.join(dealer_print)
print ' -------------- '


#class Card:

#	def __init__(self


# Dealers always hit below 17 and stick over
# Aces can be 1 or 11
# If total value < 21 then ace = 11
# If total value > 21 with aces then aces = 1

playershand = []
dealershand = []
i=0
while i < 52:
	if len(playershand) < 2:
		playershand.append(deck[i])	
		#print playershand[i][0]+playershand[i][1]
		i += 1	
	if len(dealershand) < 2:
		dealershand.append(deck[i])
		dealershand_print = [dealershand[j][0]+dealershand[j][1] for j in range(len(dealershand))]
		print "Dealer: %s" % (dealershand_print)
		i += 1

