from net import Net
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("Table Tennis")




screen.tracer(2)
net = Net()

paddle1 = Paddle()
paddle2 = Paddle()
paddle2.goto(-480, 0)
ball = Ball()

# screen.update()

#Set Controls
screen.onkey(paddle1.move_up, 'Up')
screen.onkey(paddle1.move_left, 'Left')
screen.onkey(paddle1.move_down, 'Down')
screen.onkey(paddle1.move_right, 'Right')


screen.onkey(paddle2.move_up, 'w')
screen.onkey(paddle2.move_left, 'a')
screen.onkey(paddle2.move_down, 's')
screen.onkey(paddle2.move_right, 'd')


screen.listen()
screen.exitonclick()