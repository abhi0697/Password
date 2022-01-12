from check_pwned import pwnedpassword
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
# Encrypting the generated and validated password with AES CBC mode
IV = get_random_bytes(16)
def aes_cbc_encrypt(key1, plaintext, mode=AES.MODE_CBC): 
    try:
        pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
        plaintext=pad(plaintext)
        aes = AES.new(key1, mode, IV) 
        new_data = aes.encrypt(plaintext.encode('utf8')) 
        pwnedpassword(new_data)
        return new_data 
    except Exception as e:
        print(e)
