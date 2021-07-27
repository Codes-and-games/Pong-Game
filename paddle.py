from turtle import *

class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(positions)
    #
    def up(self):
        y1 = self.ycor() + 60
        self.goto(self.xcor(), y1)


    def down(self):
        y1 = self.ycor() - 60
        self.goto(self.xcor(), y1)

