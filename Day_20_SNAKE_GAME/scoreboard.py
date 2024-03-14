from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Oswald", 12, "bold")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.count} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.count > self.high_score:
            self.high_score = self.count
            with open("data.txt", mode="w") as high_score_file:
                str_count = str(self.count)
                high_score_file.write(str_count)

        self.count = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.count += 1
        self.update_scoreboard()
