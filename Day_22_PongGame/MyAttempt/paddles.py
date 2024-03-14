from turtle import Turtle
# POSITIONS = [(-350, -20), (-350, 0), (-350, 20), (350, -20), (350, 0), (350, 20)]
class Paddles(Turtle):
    def __init__(self):
        super().__init__()

    def creating_paddles(self, coordinates):
        for position in coordinates:
            print(position)
            self.shape("square")
            self.color("white")
            self.penup()
            self.goto(position)
