from turtle import Turtle

class Score(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score=0
        self.goto(x_cor,y_cor)
        self.write(self.score,align="center",font=("Courier",80,"normal"))


    def scored(self):
        new_score=self.score+1
        self.clear()
        self.write(new_score, align="center", font=("Courier", 80, "normal"))
        self.score+=1