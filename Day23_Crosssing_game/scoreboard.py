from turtle import Turtle
FONT = ("Courier", 18, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1

    def scoreboard(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.scoreboard()

    def endgame_message(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)