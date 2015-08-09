from itertools import permutations
import enchant
from random import shuffle
from time import clock



d = enchant.Dict("en_GB")
words = []
letters = []
const = list("bcdfghjklmnpqrstvwxyz"*9)
shuffle(const)
vow = list("aeiou"*9)
shuffle(vow)

while len(letters) < 9:
	choice = input("Vowel or Consonant? (v/c) ")
	if choice == 'v':
		letters.append(vow.pop(0))
		print(letters)
	else:
		letters.append(const.pop(0))
		print(letters)


#word = ''.join(letters)
word = input("enter the word: ")

upper = int(input("smallest length word? "))

start = clock()

for i in range(upper,len(list(word))+1):
	print("Checking", i,"letter words",end="\r")
	for j in list(permutations(list(word),r=i)):
		if d.check(''.join(j))==True and ''.join(j) not in words:
			#print(''.join(j))
			words.append(''.join(j))

print(clock()-start, "seconds taken.")

print(', '.join(words))
