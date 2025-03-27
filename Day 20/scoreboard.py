from food import Food

ALIGN="center"
FONT=('Arial', 10, 'normal')


class Score(Food):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.num=0
        self.goto(0,280)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.num} ", align=ALIGN, font=FONT)

    def scored(self):
        self.num+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGN, font=('Arial', 20, 'normal'))


