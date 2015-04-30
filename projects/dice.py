import random
import func

start = raw_input("Would you like to roll the dice? (y/n) ")

if start == 'n':
	quit()

again = 'y'
while again == 'y':
	how_many = input("How many? (please enter an integer) ")
	howmany_dice = list(range(how_many))
	dice = []
	for i in howmany_dice:
		roll = random.randint(1,6)
		dice.append(roll)
	print dice
	mean_q = raw_input('Would you like to know the mean of your rolls? (y/n) ')
	if mean_q == 'y':
		print 'The mean average is:', func.mean(dice)
	med_q = raw_input('Would you like to know the median values of the rolls? (y/n) ')
	if med_q == 'y':
		print 'The median is:',func.median(dice)
	mode_q = raw_input('Would you like to know the mode(s) of your rolls? (y/n) ')
	if mode_q == 'y':
		func.modeprinted(dice)
	again = raw_input("Would you like to roll again? (y/n) ")
