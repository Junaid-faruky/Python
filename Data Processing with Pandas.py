import pandas as pd
import numpy as np

# Create sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 28, 32],
    'Salary': [50000, 60000, 70000, 55000, 65000],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR']
}

df = pd.DataFrame(data)

# Basic operations
print("DataFrame:")
print(df)
print("\nAverage salary by department:")
print(df.groupby('Department')['Salary'].mean())
print("\nPeople older than 30:")
print(df[df['Age'] > 30])
