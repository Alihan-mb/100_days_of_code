from turtle import Turtle, Screen
import random


screen = Screen()
screen.listen()
screen.setup(800, 500)
screen.bgpic("field.png")
collors = ["red", "black"]
first_team = []


for i in range(11):
    new_turtle = Turtle(shape="circle")
    new_turtle.color("red")
    new_turtle.penup()
    new_turtle.hideturtle()
    first_team.append(new_turtle)

for _ in range(1):
    x = 50
    y = - 50
    for player in first_team[:2]:
        player.showturtle()
        player.goto(x, y)
        y += 100
    for player in first_team[10:11]:
        player.showturtle()
        player.goto(360, 0)

for _ in range(3):
    y = -150
    for player in first_team[2:6]:
        player.showturtle()
        player.goto(x=150, y=y)
        y += 100

for i in range(3):
    y = -200
    for player in first_team[6:10]:
        player.showturtle()
        player.goto(x=250, y=y)
        y += 130


screen.exitonclick()