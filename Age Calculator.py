from datetime import datetime

birth = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth, "%Y-%m-%d")
today = datetime.now()
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

print(f"You are {age} years old.")
