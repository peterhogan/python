from random import randint
from random import shuffle
import operator

ops = { "+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul}

numbers = []
all_ops = ["+","-","/","*"]*6
shuffle(all_ops)
bigs = [25,50,75,100,250,500,750,1000]*6
shuffle(bigs)
smalls = [1,2,3,4,5,6,7,8,9]*6
shuffle(smalls)
print('Pick 6 numbers, big (b) or small (s)')

while len(numbers)<5:
        choice = input("b/s?: ")
        if choice == 'b':
                numbers.append(bigs.pop(0))
                print(numbers)
        elif choice == 's':
                numbers.append(smalls.pop(0))
                print(numbers)
                
print("Calculating Number using %d, %d, %d, %d and %d..." %(numbers[0],numbers[1],numbers[2],numbers[3],numbers[4]))
shuffle(numbers)
print(numbers)

counter = 1

correct_number = False
while correct_number == False:
        try:    
                to_calc = ops[all_ops[0]](numbers[0],ops[all_ops[1]](numbers[1],ops[all_ops[2]](numbers[2],ops[all_ops[3]](numbers[3],numbers[4]))))
                condition = (to_calc == round(to_calc)) and (to_calc > (0)) and (to_calc < 5)
                #condition = (to_calc == round(to_calc)) and (to_calc > 20) and (to_calc < 1000)
                if condition == True:
                        if counter > 1:
                                print("Got a sensible number after %d tries." % counter)
                        else:
                                print("Got a sensible number after 1 try.")
                        to_calc = int(to_calc)
                        correct_number = True
                else:   
                        counter += 1
                        #print("Got %f: trying again.." % to_calc)
                        shuffle(numbers)
                        shuffle(all_ops)
        except ZeroDivisionError:
                counter += 1
                #print("Division by Zero: trying again..")
                shuffle(numbers)
                shuffle(all_ops)

print(to_calc)

give_up = False

while give_up == False:
        print("Give up? (y/n)")
        ans = input("> ")
        if ans == 'y':
                give_up = True

list_to_calc = [numbers[0],all_ops[0],numbers[1],all_ops[1],numbers[2],all_ops[2],numbers[3],all_ops[3],numbers[4]]
print("%d %s (%d %s (%d %s (%d %s %d)))" % (numbers[0],all_ops[0],numbers[1],all_ops[1],numbers[2],all_ops[2],numbers[3],all_ops[3],numbers[4]))
        
	

