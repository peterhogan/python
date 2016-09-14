from random import randint
from getpass import getpass
import string

# this generates the dictionary that the cypher uses
allprint = dict((k,v) for v,k in enumerate(string.printable))

# remove the useless characters
del allprint['\t']
del allprint['\n']
del allprint['\r']
del allprint['\x0c']
del allprint['\x0b']

# construct the reverse dictionary from the allprint one
translate_dict = dict([(j,i) for i,j in allprint.items()])

# make random keys for the encrpytion that can be used later (sent to the recipient etc.)
shiftvalue_1 = randint(-93,93)
shiftvalue_2 = randint(-93,93)
while shiftvalue_1 == shiftvalue_2:
	shiftvalue_2 = randint(-93,93)
shiftvalue_3 = randint(-93,93)
while shiftvalue_2 == shiftvalue_3:
	shiftvalue_3 = randint(-93,93)

# The function for encrypting:
def encrypt(message, shift1, shift2, shift3):
	message_cyphertext_values = [] # initalise the list for the message keys

	for letter in list(message): # extract the letters from the message
		message_cyphertext_values.append(allprint[letter]) # populate the cyphertest values
	
	# index the cyphertext for ease
	message_windex = zip(range(len(message_cyphertext_values)),list(message_cyphertext_values))
	cyphertext = [] # initilise the cypertext list for the text

	# actually encrypt the message
	for index,value in message_windex:
		if index in range(len(message))[0::3]: 
			j = (value + shift1) % 95
			cyphertext.append(translate_dict[j])
		elif index in range(len(message))[1::3]:
			j = (value + shift2) % 95
			cyphertext.append(translate_dict[j])
		elif index in range(len(message))[2::3]:
			j = (value + shift3) % 95
			cyphertext.append(translate_dict[j])

	return cyphertext

def decrypt(message, shift1, shift2, shift3):
	message_decyphertext_values = [] # initalise the list for the message keys

	for letter in list(message): # extract the letters from the message
		message_decyphertext_values.append(allprint[letter]) # populate the cyphertest values
	
	# index the decyphertext for ease
	message_windex = zip(range(len(message_decyphertext_values)),list(message_decyphertext_values))
	decyphertext = [] # initilise the decypertext list for the text

	# decrypt the message
	for index,value in message_windex:
		if index in range(len(message))[0::3]: 
			j = (value - shift1) % 95
			decyphertext.append(translate_dict[j])
		elif index in range(len(message))[1::3]:
			j = (value - shift2) % 95
			decyphertext.append(translate_dict[j])
		elif index in range(len(message))[2::3]:
			j = (value - shift3) % 95
			decyphertext.append(translate_dict[j])

	return decyphertext

# the message variable is assigned by user input which is hidden by getpass
message = str(getpass("Enter the message to be encrypted: "))

encoded_message = encrypt(message,shiftvalue_1,shiftvalue_2,shiftvalue_3)
print("encypted message: %s" % ''.join(encoded_message))

decrypt_q = input("decrypt? (y/n) ")

if decrypt_q == 'y':
	decoded_message = decrypt(encoded_message,shiftvalue_1,shiftvalue_2,shiftvalue_3)
	print("message was: ")
	print(''.join(decoded_message))

message = str(getpass("Enter the message to be encrypted: "))
encoded_message = encrypt(message,1,2,3)
print("encypted message: %s" % ''.join(encoded_message))
decoded_message = decrypt(encoded_message,1,2,3)
print("decrypted message: %s" % ''.join(decoded_message))


