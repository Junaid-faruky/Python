import random

num = random.randint(1, 100)
guess = 0
tries = 0

while guess != num:
    guess = int(input("Guess a number (1-100): "))
    tries += 1
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")

print(f"Correct! It took you {tries} tries.")
