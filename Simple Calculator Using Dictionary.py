def calculator(a, b, op):
    operations = {
        "+": a+b,
        "-": a-b,
        "*": a*b,
        "/": a/b if b != 0 else "Division by zero!"
    }
    return operations.get(op, "Invalid operator")

print(calculator(10, 5, "*"))
