# 31. Lambda function
add = lambda x, y: x + y

# 32. Factorial
def fact(n): return 1 if n == 0 else n * fact(n-1)

# 33. Fibonacci (iterative)
a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b

# 34. Prime check
def is_prime(n): return all(n%i for i in range(2, int(n**0.5)+1)) if n>1 else False

# 35. Even/odd
num % 2 == 0

# 36. Palindrome
s == s[::-1]

# 37. List sum
sum([1, 2, 3])

# 38. Sort dictionary by value
sorted(d.items(), key=lambda x: x[1])

# 39. Use of map()
list(map(str, [1,2,3]))

# 40. Use of filter()
list(filter(lambda x: x%2==0, range(10)))
