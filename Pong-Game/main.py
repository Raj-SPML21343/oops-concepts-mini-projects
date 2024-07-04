from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")

screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()

# print(l_paddle)
screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect Collision with top or bottom wall and bounce back the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > r_paddle.xcor() - 25:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < l_paddle.xcor() + 25:
        ball.bounce_x()
    # Detect if right paddle misses
    if ball.xcor() > r_paddle.xcor() + 30:
        ball.reset_position()
        scoreboard.l_point()
    # Detect if left paddle misses
    if ball.xcor() < l_paddle.xcor() - 30:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
