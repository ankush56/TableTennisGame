from turtle import Turtle,Screen

class Net(Turtle):
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.color("white")
        self.turtle.pendown()
        self.turtle.goto(0, 300)
        self.turtle.goto(0, -300)
        self.turtle.hideturtle()
        self.turtle.shape()

