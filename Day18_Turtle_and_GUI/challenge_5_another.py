from turtle import Turtle, Screen
import random

timmy = Turtle()
directions = [0, 90, 180, 270]
screen = Screen()
screen.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def drawing(colour, gap):
    timmy.speed(50)
    timmy.pencolor(colour)
    timmy.right(gap)
    timmy.circle(100)


gap = 7
for i in range(int(360 / gap)):
    ran_colour = random_colour()
    drawing(ran_colour, gap)


screen.title("TURTLE GAME")
screen.exitonclick()
