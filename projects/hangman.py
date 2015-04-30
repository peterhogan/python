import random
import string

#def hash(input):
	

words = {1:'abruptly', 
2:'hello', 
3:'cobweb', 
4:'equip', 
5:'galvanize', 
6:'ivy', 
7:'jumbo', 
8:'swivel', 
9:'topaz', 
10:'vortex', 
11:'wizard', 
12:'xylophone', 
13:'yachtsman', 
14:'zephyr', 
15:'zilch', 
16:'zodiac'} 

play = raw_input("So you want to play hangman? (y/n) ")
if play =='n':
	quit()

current_word = words[random.randint(1,16)]
#print current_word
current_word_letters = list(current_word)
#print current_word_letters

obs_word = list(len(current_word) * '_')
blanks = ' '.join(obs_word)
print blanks

#print current_word_letters
print 'There are %d letters to guess' % len(current_word_letters)
again = 'y'
guess = 1

while again == 'y':
	print "Guess #%d - pick a letter" % guess

	while True:
	    letter_guess = raw_input(':')
	    if len(letter_guess) == 1:
	        if letter_guess in string.letters:
	            break
	        print 'Please enter only letters'
	    else:
       		print 'Please enter only one character'

	guess_lc = letter_guess.lower()
	if guess_lc in current_word:
		print "Correct!"
		where = [i for i,j in enumerate(current_word_letters) if j == guess_lc] 
		for i in obs_word:
			obs_word.replace(
		for i in where:
			del obs_word[i]
		for i in where:
			obs_word.insert(i, guess_lc)
		print ' '.join(obs_word)
	else:
		print "Try again, %s" % ' '.join(obs_word)
