from turtle import Turtle
import random
COLORS = ["red", "green", "blue", "yellow", "white", "orange"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        food = self.shape("circle")
        self.penup()
        self.color(random.choice(COLORS))
        random_x = random.randint(-360, 360)
        random_y = random.randint(-260, 260)
        self.shapesize(0.5, 0.5)
        self.goto(random_x, random_y)


    def creating_food(self):
        self.color(random.choice(COLORS))
        self.shapesize(0.5, 0.5)
        random_x = random.randint(-360, 360)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)