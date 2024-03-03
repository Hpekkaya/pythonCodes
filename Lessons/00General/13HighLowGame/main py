from art import logo, vs
from game_data import data
import random
import os


def format_account(acnt):
    """Takes the account Data and returns it printable format"""
    acnt_name = acnt["name"]
    acnt_desc = acnt["description"]
    acnt_country = acnt["country"]
    return f"{acnt_name}, {acnt_desc}, from {acnt_country}"


def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and followers acount and returns it if they it got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
print(logo)
score = 0
game_should_continue = True
#  Generate random account from the data
account_b = random.choice(data)


# Make the game repeatable
while game_should_continue:

    # Making account at position B become the next account at position A
    account_a = account_b
    account_a = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_account(account_a)}")
    print(vs)
    print(f"Against B: {format_account(account_b)}")

    # Ask users for guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #  Check if user correct
    # # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    print(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    os.system("cls" if os.name == "nt" else "clear")

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You are right! Your Current Score :{score}")
    else:
        game_should_continue = False
        print(f"Sorry that's wrong Your Current Score :{score}")
