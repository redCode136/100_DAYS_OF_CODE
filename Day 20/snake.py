from turtle import Turtle, Screen

SNAKE_BODY = [(0, 0), (-20, 0), (-40, 0)]


class Snake():
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for x in SNAKE_BODY:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.goto(x)
            self.segment.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(20)

    def up(self):
        if self.segment[0].heading() != 270:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)

    def left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)

    def right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)

    def check_in_border(self):
        print(self.head.xcor())
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:

            return False

    def extend_snake(self,t):
        if self.head.distance(t)>0:
            new_x = self.segment[0].xcor()
            new_y = self.segment[0].ycor()
            new_seg=self.segment[0].goto(new_x, new_y)
            self.segment.append(new_seg)