# AES Encrypt / Decrypt

from Crypto.Cipher import AES
import base64

msg_text = 'test some plain text here'.rjust(32)
secret_key = '1234567890123456'

cipher = AES.new(secret_key,AES.MODE_ECB)

encoded = base64.b64encode(cipher.encrypt(msg_text))
print('AES Encrypted Text : ', encoded.decode('utf8'))

decoded = cipher.decrypt(base64.b64decode(encoded))
print('AES Decrypted Text : ', decoded.strip().decode('utf8'))

# SHA Hash True Encryption

import hashlib

text = 'Abhishek'

def Encrypt(text):
    sha = \
        hashlib.sha256(text.encode()).hexdigest()
    return sha
sha = Encrypt(text)
print("\nSHA Encrypted Hashed Text : "+sha)
