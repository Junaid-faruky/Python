# 1. Swap variables
a, b = 5, 10
a, b = b, a

# 2. Reverse a string
s = "Hello"
rev = s[::-1]

# 3. Count vowels in a string
sum(1 for c in s.lower() if c in "aeiou")

# 4. Find max in a list
max([3, 7, 2])

# 5. Flatten nested list
import itertools
flat = list(itertools.chain.from_iterable([[1,2], [3,4]]))

# 6. List comprehension
squares = [x*x for x in range(10)]

# 7. Dictionary comprehension
sqr_map = {x: x**2 for x in range(5)}

# 8. Unique elements
list(set([1, 2, 2, 3]))

# 9. Merge two dicts
d1 = {'a':1}; d2 = {'b':2}; d1.update(d2)

# 10. Reverse a list
nums = [1, 2, 3]
nums.reverse()
