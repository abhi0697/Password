from check_pwned import pwnedpassword
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
# Encrypting the generated and validated password with DES CBC mode
IV = get_random_bytes(8)
def des_cbc_encrypt(key1, plaintext, mode=DES.MODE_CBC): 
    try:
        pad = lambda s: s + (8 - len(s) % 8) * chr(8 - len(s) % 8)
        plaintext=pad(plaintext)
        des = DES.new(key1, mode, IV) 
        new_data = des.encrypt(plaintext.encode('utf8')) 
        pwnedpassword(new_data)
        # print(new_data)
        return new_data 
    except Exception as e:
        print(e)
