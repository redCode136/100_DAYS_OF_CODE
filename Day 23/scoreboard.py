from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.lvl=1
        self.goto(-200,250)
        self.write(f"Level {self.lvl}" ,align="left",font=("Courier",20,"normal"))


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Courier",80,"normal"))

    def next_lvl(self):
        self.clear()
        self.lvl+=1
        self.write(f"Level {self.lvl}", align="left", font=("Courier", 20, "normal"))