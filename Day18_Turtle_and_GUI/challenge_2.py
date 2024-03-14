from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

shapes = {"triangle": 120, "square": 90, "pentagon": 72, "hexagon": 60, "heptagon": 51.5 , "octagon": 45, "nonagon": 40, "decagon": 36}
collor_list = ["royal blue", "maroon", "gold", "green", "red", "orange", "dark slate blue", "saddle brown",
               "aquamarine", "blue violet", "indigo", "light salmon	"]

def drawing(degree, collor):
    timmy.pencolor(collor)
    for i in range(3,11):
        timmy.right(degree)
        timmy.forward(100)


for item in shapes:
    collor = random.choice(collor_list)
    index_collor = collor_list.index(collor)
    collor_list.pop(index_collor)
    drawing(shapes[item], collor)


screen = Screen()
screen.title("TURTLE GAME")
screen.exitonclick()
