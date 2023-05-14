# A number guessing game - the code will select a random number between 1 and 100 and the user will try to guess it

import random

print("\nWelcome to the guessing game! Please guess a number between 1 and 100.\n\n")

# user guess input

guess = int(input("What is your guess?: "))

# generate random integer

correct_number = random.randint(1, 100)
guess_count = 1

# count guesses and let user know if guessing too high or low, loop until correct

while guess != correct_number:
  guess_count += 1
  if guess < correct_number:
    print("\nNot quite! You need to guess higher.\n")
    guess = int(input("What is your guess?: "))
  else:
    print("\nNot quite! You need to guess lower.\n")
    guess = int(input("What is your guess?: "))

print(f"\nCongrats! The right answer was {correct_number}. It took you {guess_count} guesses.\n")
