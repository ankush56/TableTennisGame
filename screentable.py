from turtle import Turtle,Screen

class ScreenTable():
    def __init__(self):
        pass


    def setup_screen(self):
        self.screen = Screen()
        self.screen.setup(1000,600)
        self.screen.bgcolor("black")
        self.screen.title("Table Tennis")
        self.screen.listen()
        self.screen.exitonclick()
