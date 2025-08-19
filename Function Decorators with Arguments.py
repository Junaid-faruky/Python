# A decorator that repeats the function call a specified number of times
def repeat(num_times):
    # This is the decorator factory
    def decorator_repeat(func):
        # This is the actual decorator
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value # Returns the value from the last call
        return wrapper_repeat
    return decorator_repeat

@repeat(num_times=4) # The decorator is called with an argument first
def greet(name):
    print(f"Hello {name}")

greet("Alice")
# Output:
# Hello Alice
# Hello Alice
# Hello Alice
# Hello Alice
