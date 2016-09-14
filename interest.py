from math import exp

amount=float(input("how much do you start with in the account?: "))

yearly_amount = float(input("How much per year is added?: "))

intr = float(input("What is the interest as a decimal? (1% would be 0.01): "))

years = int(input("How many years is it in for?: "))

for i in range(years+1):
	print("year",i,": £",amount)
	amount += yearly_amount 
	amount = amount + (amount*intr)
	

