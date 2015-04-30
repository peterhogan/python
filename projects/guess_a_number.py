import maths
import random

print "Let's guess a number."
bottom = input("Pick a range; bottom number: ")
top = input("Pick a top number? ")
guess_range = range(bottom, top+1)
ans = random.randint(bottom, top)
games = 0
average_guesses = []
again = 'y'

while again == 'y':
	ans = random.randint(bottom, top)
	games += 1
	print "Game %d: Number picked!..." % games
	guesses = 0
	guess = '' 
	while guess != ans:
		print "Guess #%d:" % (guesses+1)
		guess = input("> ")
		guesses += 1
		if guess > ans:
			print "Too high,"
		elif guess < ans:
			print "Too low,"
		else:
			pass

	if guess == ans:
		average_guesses.append(guesses)
		again = raw_input("Yes! Play again? (y/n)")
avg_guess = maths.mean(average_guesses)
print average_guesses
print "End of game, %d games played with an average of %f guesses." % (games, avg_guess)
