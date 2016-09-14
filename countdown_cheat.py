from itertools import permutations
import enchant
d = enchant.Dict("en_GB")
words = []

word = input("enter the word: ")

upper = int(input("smallest length word? "))


for i in range(upper,len(list(word))+1):
	for j in list(permutations(list(word),r=i)):
		if d.check(''.join(j))==True and ''.join(j) not in words:
			#print(''.join(j))
			words.append(''.join(j))

print(', '.join(words))
