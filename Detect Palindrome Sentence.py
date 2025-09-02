def is_palindrome(text):
    clean = "".join(c.lower() for c in text if c.isalnum())
    return clean == clean[::-1]

print(is_palindrome("A man a plan a canal Panama"))
