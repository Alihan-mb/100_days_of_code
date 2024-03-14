from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

directions = ["left", "right"]
colour_list = ["royal blue", "maroon", "gold", "green", "red", "orange", "dark slate blue", "saddle brown",
               "aquamarine", "blue violet", "indigo"]

def drawing(directions, colour, angle):
    timmy.pensize(width=5)
    #loop
    if directions == "left":
        timmy.left(angle)
    else:
        timmy.right(angle)
    timmy.pencolor(colour)
    timmy.forward(50)


for i in range(50):
    angle = random.randint(45, 90)
    d_actions = random.choice(directions)
    collorrrr = random.choice(colour_list)
    drawing(d_actions, collorrrr, angle)


screen = Screen()
screen.title("TURTLE GAME")
screen.exitonclick()
