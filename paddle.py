from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        # self.turtle = Turtle()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(4,2)
        self.goto(480, 0)