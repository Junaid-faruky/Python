import random

options = ['rock', 'paper', 'scissors']
user = input("Choose rock/paper/scissors: ").lower()
computer = random.choice(options)

if user == computer:
    result = "Draw!"
elif (user == 'rock' and computer == 'scissors') or \
     (user == 'scissors' and computer == 'paper') or \
     (user == 'paper' and computer == 'rock'):
    result = "You win!"
else:
    result = "You lose!"

print(f"Computer chose {computer}. {result}")
