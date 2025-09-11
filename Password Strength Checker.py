# 14. Password Strength Checker
import re

def check_password(pwd):
    if (len(pwd) >= 8 and re.search(r"[A-Z]", pwd) and 
        re.search(r"[a-z]", pwd) and re.search(r"[0-9]", pwd) and 
        re.search(r"[@#$%^&*!]", pwd)):
        return "Strong Password"
    return "Weak Password"

print(check_password("Hello123"))
print(check_password("Hello@123"))
