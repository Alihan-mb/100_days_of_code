#TODO 1 Painting should be 10 by 10
#TODO 2 Each do should be 20 in size
#TODO 3 Each dot should be spaced apart by 50 paces
import random
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.colormode(255)
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188),
              (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154),
              (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12)]

timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

def drawing():
    for _ in range(10):
        timmy.speed(0)
        timmy.pendown()
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)

for _ in range(10):
    drawing()
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)



screen.exitonclick()