history = []
while True:
    expr = input("Calc> ")
    if expr in ("exit","quit"): break
    try:
        result = eval(expr, {"__builtins__":{}})
        history.append(f"{expr} = {result}")
        print(result)
    except Exception as e:
        print("Error:", e)
print("Session history:")
for item in history:
    print(item)
