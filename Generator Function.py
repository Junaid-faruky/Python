def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Generate first 10 Fibonacci numbers
fib_gen = fibonacci_generator(10)
print("Fibonacci sequence:", list(fib_gen))
