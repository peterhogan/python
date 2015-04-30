import os 

firstsection = raw_input("First three octets: ") 
endoctet_begin = raw_input("Begin sweep from here: ")
endoctet_end = raw_input("End sweep here: ")

i = endoctet_begin

while i < endoctet_end:
	address = firstsection + str(i) 
	response = os.system("ping -c 1" + address) 
	if response == 0:
		print firstsection, i,  "is up."
	else:
		print firstsection, i, "is down."
	int(i) += 1


