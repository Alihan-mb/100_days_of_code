import random
from game_data import data
list_a = []
list_b = []

def sending_dict():
    random_value = random.choice(data)
    return random_value


def storing_followers(list):
    for item in list:
        del item["follower_count"]
        return (', '.join(f'{value}' for key, value in list[0].items()))


score = 0
def comparing_values(value1, value2, follower_1 , follower_2, score):
    print(f"Compare A: {value1}")
    print(f"Compare B: {value2}")
    user_decision = input("Who has more followers? Pick 'A' or 'B' ").lower()
    if user_decision == "a" and follower_1 > follower_2:
        score += 1
        return score
    elif user_decision == "b" and follower_2 > follower_1:
        score += 1
        return score
    else:
        return

def replacing_values(list_a, list_b):
    random_value = sending_dict()
    list_a[0] = random_value
    list_b[0] = random_value


list_a.append(sending_dict())
list_b.append(sending_dict())
continuing = True

while continuing:

    follower_count_a = list_a[0]["follower_count"] #follower number here
    follower_count_b = list_b[0]["follower_count"] #follower number here

    first_to_compare = storing_followers(list_a) #list without any brackets here
    second_to_compare = storing_followers(list_b) #list without any brackets here

    final = comparing_values(value1=first_to_compare, value2=second_to_compare,
                             follower_1=follower_count_a, follower_2=follower_count_b, score=score)
    if final != "None":
        score = final
        print(f"You are right, your current score is: {score}")
        replacing_values(list_a=list_a, list_b=list_b)
    else:
        print(f"You are wrong, your final score is: {score}")
        continuing = False
