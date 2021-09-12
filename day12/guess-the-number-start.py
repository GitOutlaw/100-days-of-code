# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from guess_number_art import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 5.")


def number_generator():
    """Generates a random number and returns random_number"""

    random_number = random.randint(1, 10)

    return random_number


guesses_taken = 10
computer_num = number_generator()
print(f"Pssst, the correct answer is {computer_num}")
print(f"You have 10 attempts remaining to guess the number.")


while guesses_taken > 0:
    guess = int(input("Make a guess: "))
    guesses_taken -= 1
    print(
        f"You have {guesses_taken} attempts remaining to guess the number.")

    if guess < computer_num:
        print("Too low!")
        print("Guess again.")


    if guess > computer_num:
        print("Too low!")
        print("Guess again.")
       
    if guess == computer_num:
        break

if guess == computer_num:
    guesses_taken += (guesses_taken)
    print(f"Good Job! You guess the correct number {computer_num}")

if guess != computer_num:
    computer_num = (computer_num)
    print(f"You've run out of guesses, you lose.")
