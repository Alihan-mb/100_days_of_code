from game_data import data
import random

# вывести из данных все данные помимо подписчиков
def taking_out_data(value):
    name = value["name"]
    description = value["description"]
    country = value["country"]

    return f"{name}, {description}, from {country}"

# определить угадал юзер или нет

def compare():
    if a_followers > b_followers:
        if user_input == "a":
            return True
        else:
            return False
    elif b_followers > a_followers:
        if user_input == "b":
            return True
        else:
            return False

compare_b = random.choice(data)
score = 0
should_play = True

while should_play:
    compare_a = compare_b
    compare_b = random.choice(data)
    if compare_a == compare_b:
            compare_b = random.choice(data)

    taking_out_data(value=compare_a)
    taking_out_data(value=compare_b)
    print(taking_out_data(value=compare_a))
    print(taking_out_data(value=compare_b))

    a_followers = compare_a["follower_count"]
    b_followers = compare_b["follower_count"]
    print(a_followers)
    print(b_followers)

    user_input = input("Who has more followers? Type 'A' or 'B' ").lower()

    if compare() == True:
        score += 1
        print(f"You guessed correctly, current score is {score}")
    else:
        print(f"You are wrong, final score is: {score}")
        should_play = False


# если юзер угадал данные из переменной б, становяться данные из переменной а

# если юзер проиграл, выводим итоговый счет и игра заканчивается. Если узер угадал, игра продолжается, счет увеличивается