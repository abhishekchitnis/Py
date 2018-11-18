# Python By Abhishek
# This program creates a secret message using a simple encryption algorithm
# called a Caesar cipher, which shifts each letter ahead by 3 places.
# The program can also decode an encoded message using the opposite algorithm.
#
# Sample log of execution:
# Your message to encode? Attack the zombies at dawn!
# The encoded message is: dwwdfn wkh crpelhv dw gdzq!

# A helper that can perform either encryption or decryption, shifting every
# letter by the given number of places, wrapping around as necessary.
import random
def helper(message, shift):
	message = message.lower()
	secret = ""
	for c in message:
		if c in "abcdefghijklmnopqrstuvwxyz":
			num = ord(c)
			num += shift
			if num > ord("z"):     # wrap if necessary
				num -= 26
			elif num < ord("a"):
				num += 26
			secret = secret + chr(num)
		else:
			# don't modify any non-letters in the message; just add them as-is
			secret = secret + c
	return secret

#Random
rnd = random.randint(1,28)
print(rnd)

# Encrypts the given string using a Caesar cipher and returns the result.
def encrypt(message):
	return helper(message, rnd)

# Decrypts a string that was previously encrypted using a Caesar cipher and returns the result.
def decrypt(message):
	return helper(message, -rnd)


# main program
msg = input("Your message to encode? ")
if len(msg) > 0:
	# wants to encrypt
	secret = encrypt(msg)
	print("The encoded message is:", secret)
else:
	# empty message; wants to decrypt
	secret = input("Your message to decode? ")
	if len(secret) > 0:
		msg = decrypt(secret)
		print("The decoded message is:", msg)