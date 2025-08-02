from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import json

KEY = b"16byteslongkey!!"  # store securely in real use

def pad(s):
    return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

def encrypt(plaintext):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(pad(plaintext).encode())).decode()

def decrypt(ciphertext):
    cipher = AES.new(KEY, AES.MODE_ECB)
    data = cipher.decrypt(base64.b64decode(ciphertext))
    pad_len = data[-1]
    return data[:-pad_len].decode()

# Example usage
vault = {"gmail": encrypt("mygmailpassword"), "github": encrypt("myghpass")}
print("Encrypted vault:", json.dumps(vault))
print("Decrypted gmail:", decrypt(vault["gmail"]))
