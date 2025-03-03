from multiprocessing.spawn import import_main_path
from paddle import Paddle
from turtle import Screen
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

score = Scoreboard()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
screen.listen()

screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.y_bounce()

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()>-350:
        ball.x_bounce()

    if ball.xcor()>380:
        ball.reset()
        score.l_point()

    if ball.xcor()<-380:
        ball.reset()
        score.r_point()

screen.exitonclick()