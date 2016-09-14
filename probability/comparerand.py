import randomdev
import random


devlist = []
randlist = []

#x = random.randint(1,100)

for i in range(1,100):
	x = random.randint(1,100)
	if x not in randlist:
		randlist.append(x)
	else:
		break
#print(randlist)
print("random.rantint ",len(randlist))

for i in range(1,100):
	y = randomdev.randint(1,100)
	if y not in devlist:
		devlist.append(y)
	else:
		break
#print(devlist)
print("randomdev.randint ", len(devlist))
