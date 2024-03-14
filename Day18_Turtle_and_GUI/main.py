from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
screen.colormode(255)
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188),
              (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154),
              (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12)]

position = -300
def drawing_circle():
    for i in range(10):
        random_color = random.choice(color_list)
        timmy.color(random_color)
        timmy.pendown()
        timmy.begin_fill()
        timmy.circle(0.2)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(1)



for i in range(10):
    timmy.penup()
    timmy.setx(position)
    timmy.sety(position)
    # screen.setworldcoordinates(-1, position, 10, 10)
    random_color = random.choice(color_list)
    drawing_circle()
    position = position + 50













screen.exitonclick()