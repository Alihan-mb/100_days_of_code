from turtle import Turtle, Screen
from paddles import Paddles

LEFT_PADDLE = [(-350, -20), (-350, 0), (-350, 20)]
RIGHT_PADDLE = [(350, -20), (350, 0), (350, 20)]
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)

left_paddle = Paddles()
right_paddle = Paddles()
for _ in range(3):
    left_paddle.creating_paddles(LEFT_PADDLE)
    right_paddle.creating_paddles(RIGHT_PADDLE)


screen.exitonclick()