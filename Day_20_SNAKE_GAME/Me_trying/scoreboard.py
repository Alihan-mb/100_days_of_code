from turtle import Turtle
FONT = ("Oswald", 12, "bold")
FONT1 = ("Oswald", 20, "bold")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=-250, y=260)
        self.color("white")
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT)

    def update_score(self):
        self.score += 1
        self.scoreboard()

    def game_over(self):
        self.goto(-100, 0)
        self.write("GAME OVER", font=FONT1)