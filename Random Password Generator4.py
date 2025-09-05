import random, string

def generate_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

print(generate_password(12))
