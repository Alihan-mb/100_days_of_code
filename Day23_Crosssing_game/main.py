import time
from turtle import Screen
from player import Player
from car_manager import CarManager, increase_speed
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
scoreboard.scoreboard()

screen.onkeypress(player.moving_forward, "w")
screen.onkey(player.moving_back, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.moving_cars()

    for car in car_manager.cars:
        if player.distance(car) <= 20:
            scoreboard.endgame_message()
            time.sleep(2)
            game_is_on = False

    if player.finish_line():
        scoreboard.increase_score()
        increase_speed()

screen.exitonclick()
