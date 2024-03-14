from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

for i in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = Screen()
screen.title("TURTLE GAME")
screen.exitonclick()
