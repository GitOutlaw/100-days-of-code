from higher_lower_art import logo, vs
from higher_lower_game_data import data
from replit import clear
import random


def get_random_account():
    """Gets data from random account."""

    return random.choice(data)


def format_data(account):
    """Formats data and returns fstring with variables"""

    name = account["name"]
    description = account["description"]
    country = account["country"]
    answer = account["follower_count"]

    # Used for testing. Shows how "follower_count" from data.
    return f"{name}, a {description}, from {country}. Pssst the answer: {answer}"

    # return f"{name}, a {description}, from {country}."


def check_answer(guess, a_followers, b_followers):
    """Checks follower_count against user's guess 
    and returns True if it's right.
    Or False if it's wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    """Executes higher lower game. """
    # Prints logo from higher_lower_art.py
    print(logo)

    # Sets intial score to 0
    score = 0

    # Sets game_should_continue intial value
    game_should_continue = True

    # Outputs
    account_a = get_random_account()
    account_b = get_random_account()

    # First while statement - game_should_ continue
    while game_should_continue:
        #
        account_a = account_b
        account_b = get_random_account()

        # Nested while loop
        while account_a == account_b:
            account_b = get_random_account()

        # Prints formated_data in fstring
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against: B: {format_data(account_b)}")

        # User input requesting guess, then format using .lower()
        guess = input("Who has more followers? Type 'A' or 'B':").lower()

        # Gets follower count from higher_lower_data
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Checks the answer from check_answer()
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Executes the clear() function from replit
        clear()

        # Prints logo again from higher_lower_art.py
        print(logo)

        # Scores the game
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")

        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score {score}")


game()
