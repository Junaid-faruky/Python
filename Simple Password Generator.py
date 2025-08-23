import secrets
import string

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

# Generate a secure password
new_password = generate_password()
print(f"Your new password: {new_password}")
