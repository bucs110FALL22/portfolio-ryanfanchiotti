import random

number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10"))
for i in range(0,2):
  if number == guess:
    print("Correct")
    exit()
  if number < guess: 
    print("Too high")
    guess = int(input("Guess again"))
  if number > guess:
    print("Too low")
    guess = int(input("Guess again"))
print("Incorrect, the correct number was", number)
