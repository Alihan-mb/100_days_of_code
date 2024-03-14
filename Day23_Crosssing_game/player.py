from turtle import Turtle


STARTING_POSITION = (0, -260)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.starting_point()

    def starting_point(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def moving_forward(self):
        self.forward(MOVE_DISTANCE)

    def moving_back(self):
        self.backward(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.starting_point()
            return True










