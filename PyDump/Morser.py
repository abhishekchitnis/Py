import hashlib
import random

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    ' ':'/', '.':'.-.-.-', ',':'--..--',
    ':':'---...', '?':'..--..', "'":'.----.',
    '-':'-....-', '/':'-..-.', '@': '.--.-.',
    '=':'-...-', '(':'-.--.', ')':'-.--.-',
    '+':'.-.-.'
    }

CODE_REVERSED = {value:key for key,value in CODE.items()}

text = input('\nEnter Text to Encrypt : ')

#Random
rnd = random.randint(1,28)
print(rnd)

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
	
def encrypt(msg):
	return helper(msg, rnd)

def decrypt(message):
	return helper(message, -rnd)

enc = encrypt(text)

print('\nEncrypting Text to Random : '+enc)

def to_morse(s):
    return ' '.join(CODE.get(i.upper()) for i in s)

def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())

mor = to_morse(enc)	
print("\nReEncrypting Random Text to Morse Code : "+mor)

mortohsh = from_morse(mor)

print("\nDecrypting Morse Code to Random Text : "+mortohsh.lower())

dec = decrypt(mortohsh.lower())

print("\nReDecrypting Morse Code to Text : "+dec)

input("\n\nPress [ENTER] to Exit")