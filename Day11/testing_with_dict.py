import random

dict = {
    "Fallout": 2,
    "Dying Light": 5,
    "GTA": 7,
    "They are billions": 1,
    "Fifa": 4,
    "Leo": 3,
    "Shrek": 3,
    "Kong": 2,
    "Witcher": 8,
    "Max Payne": 5
}
def i_spread_games():
    '''Распределяет игры'''
    rand_game_name = random.choice(list(dict.keys()))
    rand_value = dict[rand_game_name]
    return rand_value

def calculate_game_score(list_of_games):
    return sum(list_of_games)


user = []
pc = []
playing = True
while playing:
    def playing_the_game():

        for i in range(3):
            user.append(i_spread_games())
            pc.append(i_spread_games())

        print(f" User Score is {calculate_game_score(user)}, his games are {user}")
        print(f" PC Score is {calculate_game_score(pc)}, PC games are {pc}")


    while input("Do you want to try? Type 'Y' if yes, type 'N' if no ").lower() == "y":
        playing_the_game()

