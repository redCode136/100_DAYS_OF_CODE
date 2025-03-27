from turtle import Turtle

class Pong(Turtle):
    def __init__(self,xcor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("White")
        self.shapesize(5,1)
        self.goto(xcor,0)

    def go_up(self):
        new_y=self.ycor()+10
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y=self.ycor()-10
        self.goto(self.xcor(),new_y)
