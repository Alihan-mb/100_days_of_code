# the game must have a function to distribute accounts DONE
# we have to ask the user to pick A or B
# if it's a correct guess, we add to the score 1, if the answer is wrong we display the final score
# if it's a correct guess, we take option b and turn it into option a
# we have to make the game repeatable if the answer is correct

from game_data import data
import random

def distributing_accounts():
    account = random.choice(data)
    return account

def printing_the_essentinal_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    print(f"{name} is, {description} from {country}")

def checking_the_guess(val1, val2, guess):
    if val1 > val2:
        if guess == "a":
            return True
        else:
            return False
    elif val2 > val1:
        if guess == "b":
            return True
        else:
            return False


score = 0
option_b = distributing_accounts()
going = True
while going:
    option_a = option_b
    option_b = distributing_accounts()

    if option_a == option_b:
        option_b = distributing_accounts()

    printing_the_essentinal_data(option_a)
    printing_the_essentinal_data(option_b)

    guess = input("Who has more followers? Pick 'A' or 'B' ").lower()
    followers_a = option_a["follower_count"]
    followers_b = option_b["follower_count"]

    final = checking_the_guess(val1=followers_a, val2=followers_b, guess=guess)

    if final == True:
        score += 1
        print(f"That's a correct guess, your current score is: {score}")
    else:
        print(f"Unfortunately, that's wrong, your final score is: {score}")
        going = False














