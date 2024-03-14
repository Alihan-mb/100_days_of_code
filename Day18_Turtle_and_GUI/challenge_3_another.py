from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
directions = [0, 90, 180, 270]
screen = Screen()
screen.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def drawing(directions, colour):
    timmy.speed("fast")
    timmy.pensize(random.randint(2,15))
    timmy.setheading(directions)
    timmy.pencolor(colour)
    timmy.forward(50)


for i in range(50):
    ran_colour = random_colour()
    d_actions = random.choice(directions)
    drawing(d_actions, ran_colour)


screen.title("TURTLE GAME")
screen.exitonclick()
