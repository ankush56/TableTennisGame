from net import Net
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("Table Tennis")

screen.tracer(0)
net = Net()

right_paddle = Paddle(480, 0)
left_paddle = Paddle(-480, 0)
ball = Ball()

#Set Controls
screen.listen()
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')
screen.onkey(left_paddle.move_up, 's')
screen.onkey(left_paddle.move_down, 'x')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 260:
        ball.side_collision()

    if ball.distance(right_paddle) < 20:
        print("Hit right paddle")
        ball.paddle_collision()

    # if ball.xcor() > 300:
    #     print("collision close")
    #     ball.paddle_collision()

    #
    # if ball.xcor() > -280:
    #     ball.side_collision()



screen.exitonclick()