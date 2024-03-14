from game_data import data
import random

def forman_data(account):
    '''Forman the account data.txt into printable forman'''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    '''Use if statement to check if user is correct and returns if it's True or False'''
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
account_b = random.choice(data)
game_should_continue = True

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {forman_data(account_a)}")
    print(f"Against B: {forman_data(account_b)}")

    user_guess = input("Who has more followers? Type 'A' or 'B' ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right, current score is {score}")
    else:
        print(f"Sorry, that's wrong, final score is {score}")
        game_should_continue = False











