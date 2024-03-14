import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(800, 600)
screen.listen()
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkeypress(snake.going_up, "Up")
screen.onkeypress(snake.going_down, "Down")
screen.onkeypress(snake.going_left, "Left")
screen.onkeypress(snake.going_right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.moving_turtle()
    if snake.head.distance(food) < 20:
        food.creating_food()
        snake.extand()
        scoreboard.update_score()

    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_on = False

    for t in snake.turtles[1:]:
        if snake.head.distance(t) < 10:
            scoreboard.game_over()
            time.sleep(2)
            game_on = False


screen.exitonclick()
