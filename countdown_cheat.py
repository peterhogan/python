from itertools import permutations
import enchant
d = enchant.Dict("en_GB")
words = []

word = input("enter the word: ")

lower = int(input("smallest length word? "))

for i in range(lower,len(list(word))+1):
    allperms = list(permutations(list(word),r=i))
    for j in allperms:
        wrd = ''.join(j)
        wcheck = d.check(wrd)
        if wcheck and wrd not in words:
            words.append(wrd)

print(', '.join(words))
