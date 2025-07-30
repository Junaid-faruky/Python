from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
enc = cipher.encrypt(b"Secret Data")
print("Encrypted:", enc)
print("Decrypted:", cipher.decrypt(enc))
