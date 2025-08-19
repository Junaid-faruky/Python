# Classic way (without walrus)
data = get_data()
while data is not None:
    process(data)
    data = get_data()

# Modern way (with walrus): cleaner and avoids repetition
while (data := get_data()) is not None:
    process(data)

# In a list comprehension
numbers = [1, 2, 3, 4, 5]
filtered = [n for n in numbers if (square := n**2) > 10]
print(filtered) # Output: [4, 5]
print(square) # Output: 25 (remains in scope after the comprehension)
