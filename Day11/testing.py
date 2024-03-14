import random
def i_spread_games():
    '''Распределяет игры'''
    game_list = ["Fallout", "Dying Light", "Skyrim", "GTA", "They are billions", "Fifa", "Leo", "Shrek", "Kong",
                 "Witcher", "Max Payne"]
    game = random.choice(game_list)
    game_list.remove(game)
    return game

def calculate_game_score(list_of_games):
    if "Fallout" in list_of_games:
        return 5
    if "Dying Light" in list_of_games:
        return 6
    if "Max Payne" in list_of_games:
        return 7
    else:
        return 3

user = []
pc = []
def playing_the_game():
    user = []
    pc = []

    for i in range(3):
        user.append(i_spread_games())
        pc.append(i_spread_games())

    print(f" User Score is {calculate_game_score(user)}, his games are {user}")
    print(f" PC Score is {calculate_game_score(pc)}, PC games are {pc}")


while input("Do you want to try? Type 'Y' if yes, type 'N' if no ").lower() == "y":
    playing_the_game()

