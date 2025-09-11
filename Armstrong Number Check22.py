# 8. Armstrong Number Check
def is_armstrong(num):
    power = len(str(num))
    return num == sum(int(d)**power for d in str(num))

print(is_armstrong(153))
print(is_armstrong(123))
