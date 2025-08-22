# Sorting with lambda
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# Sort by grade descending
sorted_students = sorted(students, key=lambda x: x['grade'], reverse=True)
print("Sorted by grade:", sorted_students)

# Using lambda with map and filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Squared: {squared}")
print(f"Even numbers: {even_numbers}")
