# 6. Simple Calculator (Functions + Input)
def calculator(a, b, op):
    if op == '+': return a+b
    if op == '-': return a-b
    if op == '*': return a*b
    if op == '/': return a/b
    return "Invalid"

print(calculator(10, 5, '*'))
