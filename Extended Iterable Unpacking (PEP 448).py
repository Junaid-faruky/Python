# Using * to grab the middle of a list
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)    # Output: 5

# Combining lists
list1 = [1, 2]
list2 = [3, 4]
combined = [*list1, *list2, 5]
print(combined) # Output: [1, 2, 3, 4, 5]

# Merging dictionaries (Python 3.5+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2, 'e': 5}
print(merged_dict) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
