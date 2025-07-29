import random

number = random.randint(1, 100)
guess = None

while guess != number:
    guess = int(input("Guess (1-100): "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct!")
