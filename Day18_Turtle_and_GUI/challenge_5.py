from turtle import Turtle, Screen
import random
#Todo 1 сделать так чтобы черепаха рисовала круги
#Todo 2 сделать так, чтобы каждый раз черепаха порачивалась по своей оси на пару углов
#Todo 3
timmy = Turtle()
directions = [0, 90, 180, 270]
screen = Screen()
screen.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def drawing(directions, colour):
    timmy.speed(50)
    timmy.pencolor(colour)
    timmy.right(5)
    timmy.circle(100)


for i in range(150):
    ran_colour = random_colour()
    d_actions = random.choice(directions)
    drawing(d_actions, ran_colour)


screen.title("TURTLE GAME")
screen.exitonclick()
