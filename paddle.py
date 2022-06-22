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


    # Set Controls
    def move_up(self):
        curr_x = self.xcor()
        curr_y = self.ycor()
        self.goto(curr_x, curr_y + 20)

    def move_left(self):
        self.back(20)

    def move_down(self):
        curr_x = self.xcor()
        curr_y = self.ycor()
        self.goto(curr_x, curr_y - 20)

    def move_right(self):
        self.forward(20)