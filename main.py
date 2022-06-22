from net import Net
from turtle import Turtle, Screen
from paddle import Paddle

# screen = ScreenTable()
# screen.setup_screen()


screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("Table Tennis")
screen.tracer(0)
net = Net()

paddle1 = Paddle()
paddle2 = Paddle()
paddle2.goto(-480, 0)
screen.update()


screen.listen()
screen.exitonclick()