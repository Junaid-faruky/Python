import random, string

def shorten_url(url, length=6):
    short = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return f"http://short.url/{short}"

print("Shortened URL:", shorten_url("https://example.com"))
