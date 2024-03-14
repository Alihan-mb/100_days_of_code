import random
from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(20, 0), (0, 0), (-20, 0)]

COLORS = ["red", "white", "green", "blue", "yellow"]
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.turtles = []
        self.creating_snake()
        self.head = self.turtles[0]

    def creating_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.color(random.choice(COLORS))
        turtle.goto(position)
        self.turtles.append(turtle)

    def moving_turtle(self):
        for segment in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[segment - 1].xcor()
            new_y = self.turtles[segment - 1].ycor()
            self.turtles[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extand(self):
        self.add_segment(self.turtles[-1].position())

    def going_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def going_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def going_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def going_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
