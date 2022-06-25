from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.turtle = Turtle()
        self.color("white")
        self.penup()
        self.speed(1)
        self.shape("circle")
        self.goto(0, 0)
        self.x1 = 10
        self.y1 = 10

    def move_ball(self):
       new_x = self.xcor() + self.x1
       new_y = self.ycor() + self.y1
       self.goto(new_x, new_y)

    def side_collision(self):
        self.y1 = self.y1 * -1
        print(self.x1)

    def paddle_collision(self):
        self.x1 = self.x1 * -3
        print(self.x1)
