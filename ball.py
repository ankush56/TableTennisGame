from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.turtle = Turtle()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.goto(0, 20)