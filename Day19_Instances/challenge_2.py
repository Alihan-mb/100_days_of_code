import turtle
from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.listen()
screen.setup(500, 400)
bet = screen.textinput("TURTLE RACE", "Pick your turtle: Choose the colour").lower()

colours = ["red", "green", "blue", "yellow", "black", "brown"]
y_positions = [-70, -40, -10, 20, 50, 80]

x = 230
y = -190
for i in range(10):
    timmy = Turtle(shape="square")
    timmy.penup()
    timmy.goto(x, y)
    timmy.stamp()
    x -= 20
    y += 20
    timmy.goto(x, y)
    timmy.stamp()
    y += 20
    x += 20

list_of_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    list_of_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in list_of_turtles:
        if turtle.xcor() > 180:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won, the winning color is {winning_color}")
            else:
                print(f"You've lost, the winning color is {winning_color}")
            break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)






screen.exitonclick()