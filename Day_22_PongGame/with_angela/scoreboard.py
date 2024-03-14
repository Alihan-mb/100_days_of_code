from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-150, 260)
        self.write(f"Score: {self.left_score}", font=("Oswald", 20, "bold"))
        self.goto(100, 260)
        self.write(f"Score: {self.right_score}", font=("Oswald", 20, "bold"))

    def increase_score_left(self):
        self.left_score += 1
        self.update_score()

    def increase_score_right(self):
        self.right_score += 1
        self.update_score()
