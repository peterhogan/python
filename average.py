import random
print "Let's generate some random numbers."
bottom = input('From where...(lowest number) ')
top = input('to where... (highest number) ')
how_many = input('How many numbers would you like? ')

list = list(range(how_many))
dice = []
for i in list:
	roll = random.randint(bottom,top)
	dice.append(roll)

print dice
print "The average of these numbers is..."
print sum(dice), 'divided by', how_many, '=', float(sum(dice))/how_many
