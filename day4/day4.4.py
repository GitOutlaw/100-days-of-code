import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_action = input("Enter a choice (rock, paper, scissors): ")

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players chose {user_action}, its a Tie!")

elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose!")

elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cut paper! You win")
    else:
        print("Rock smashes scissors! You lose!")

elif user_action == "paper":
    if computer_action == "rock":
        print("Rock covers paper! You win!")
    else:
        print("Scissors cut paper! You lose!")
