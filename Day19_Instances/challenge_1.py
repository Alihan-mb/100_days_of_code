#TODO 1 - Write a function using even listener which will allow move around with WASD and clear with C

from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.listen()

def move_forward():
    timmy.forward(20)
def move_back():
    timmy.backward(20)
def turn_right():
    timmy.right(15)
def turn_left():
    timmy.left(15)

def reset():
    timmy.reset()

screen.onkeypress(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=reset)

screen.exitonclick()