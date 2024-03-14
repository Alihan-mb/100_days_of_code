import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")

screen.setup(800, 600)
screen.title("PONG GAME")
screen.listen()
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score_board = Scoreboard()

screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.ball_moving()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 40 and ball.xcor() > 300 and ball.x_move > 0 or ball.distance(l_paddle) < 40 and ball.xcor() < -300 and ball.x_move < 0:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset()
        score_board.increase_score_left()

    if ball.xcor() < -400:
        ball.reset()
        score_board.increase_score_right()


screen.exitonclick()
