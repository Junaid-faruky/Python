import pandas as pd

# Create a simple DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['NYC', 'London', 'Berlin']}
df = pd.DataFrame(data)

# Filter data and calculate average age
londoners = df[df['City'] == 'London']
avg_age = df['Age'].mean()
print(f"Average Age: {avg_age}")
print(londoners)
