from random import randint
from random import shuffle
import operator

ops = { "+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul}

all_ops = ["+","-","/","*"]*6
shuffle(all_ops)
bigs = [25,50,75,100,250,500,750,1000]*6
shuffle(bigs)
smalls = [1,2,3,4,5,6,7,8,9]*6
shuffle(smalls)
                
numbers = [bigs[0],smalls[0],smalls[1],smalls[2],bigs[1]]
#numbers = [bigs[0],smalls[0],smalls[1],smalls[2],bigs[1]]

print(numbers)
print("Calculating Number....")
shuffle(numbers)

counter = 1

correct_number = False
while correct_number == False:
        try:
                to_calc = ops[all_ops[0]](numbers[0],ops[all_ops[1]](numbers[1],ops[all_ops[2]](numbers[2],numbers[3])))
                condition = (to_calc == round(to_calc)) and (to_calc > 30) and (to_calc < 1000)
                if condition == True:
                        if counter > 1:
                                print("Got a sensible number after %d tries." % counter)
                        else:
                                print("Got a sensible number after 1 try.")
                        correct_number = True
                else:
                        counter += 1
                        print("Got %f: trying again.." % to_calc)
                        shuffle(numbers)
                        shuffle(all_ops)
        except ZeroDivisionError:
                counter += 1
                print("Division by Zero: trying again..")
                shuffle(numbers)
                shuffle(all_ops)
        

print("The number to find is: ")
print(to_calc)
        
list_to_calc = [numbers[0],all_ops[0],numbers[1],all_ops[1],numbers[2],all_ops[2],numbers[3]]
print(list_to_calc)
