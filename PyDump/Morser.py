import hashlib

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

def Encrypt(text):
    sha = \
        hashlib.sha256(text.encode()).hexdigest()
    return sha
sha = Encrypt(text)
print("\nEncrypted Hashed Value : "+sha)

def to_morse(s):
    return ' '.join(CODE.get(i.upper()) for i in s)

def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())

mor = to_morse(sha)	
print("\nReEncrypting Hashed Value to Morse Code : "+mor)

mortohsh = from_morse(mor)

print("\nDecrypting Morse Code to Hashed Value : "+mortohsh.lower())

def Decrypt(mortohsh):
    shatotext = \
        hashlib.sha256(mor.decode()).hexdigest()
    return shatotext
shatotext = Decrypt(mortohsh)
print("\nReDecrypting Morse Code to Text : "+shatotext)

input("\n\nPress [ENTER] to Exit")