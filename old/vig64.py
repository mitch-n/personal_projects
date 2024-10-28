"""
Vig64 encoding.

Converts a message to base64, then performs a vigenere cipher on the b64 string.
"""


import requests, re, base64


def vigenere(message, key, decode = False):
	#Make sure password is just letters
	if re.search("[^A-Za-z]",key):
		print("key can only contain letters.")
		return 0
	
	#Encode message to b64 for encoding
	if not decode:
		message = base64.b64encode(message.encode('utf-8')).decode('utf-8')
	
	key = key.lower()
	letters = list("abcdefghijklmnopqrstuvwxyz")
	letter_map = letters.copy()
	
	# Reverse letter_map for decoding. Simulates subtraction
	if decode:
		letter_map.reverse()
	
	# Do the vigenere cipher
	output = ""
	for i in range(len(message)):
		try:
			output += letter_map[(letter_map.index(message[i]) + letters.index(key[i % len(key)])) % len(letters)]
		except ValueError:
			output += message[i]
	
	#Decode message from b64 for decoding
	if decode:
		output = base64.b64decode(output.encode('utf-8')).decode('utf-8')

	return output
	

while True:
	print("What would you like to do?")
	print("1: Encode")
	print("2: Decode")
	print("0: Quit")
	action = input()
	print()
	
	if action == "1":
		decode = False
	elif action == "2":
		decode = True
	elif action =="0":
		break
	else:
		"Bad Input."
		continue
	
	message = input("What is your message?\n")
	print()
	key = input("What is your key?\n")
	print()
	print("--------------")
	print(vigenere(message, key, decode))
	print("--------------")
	print()

