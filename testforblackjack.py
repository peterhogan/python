hand = ['A',2,3,4,10]

print hand

value = 0

for i in hand:
	if i == 'A':
		if value + 11 > 21:
			value += 1 
		else:             
			value += 11 
	else:
		if value + i > 21 and (hand.count('A') > 0 or 'A' in hand):
			value += i
			value -= 10	
		else:	
			value += i
	print value

if 'A' in hand and value > 21:
	print aces

hand2 = [('A','S'),(10,'C'),(8,'H')]

print hand2[,0].count('A') 
