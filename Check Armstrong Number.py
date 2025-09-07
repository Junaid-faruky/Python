def is_armstrong(num):
    power = len(str(num))
    return num == sum(int(digit)**power for digit in str(num))

print(is_armstrong(153))  # True
print(is_armstrong(9474)) # True
print(is_armstrong(123))  # False
