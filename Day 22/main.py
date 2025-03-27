from turtle import Turtle, Screen
from Pong import Pong
from Ball import Ball
from scoreboard import Score
import time

sleep_param=0.1


screen=Screen()
screen.tracer(0)
screen.setup(800,600)
screen.bgcolor("Black")
screen.title("Ping Pong")



l_paddle=Pong(-350)
r_paddle=Pong(350)
ball=Ball()

screen.listen()
r_score=Score(100,200)
l_score=Score(-100,200)
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on=True
while game_is_on:
    time.sleep(sleep_param)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    #detect collition with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-340:
        print("made contact")
        sleep_param/=1.2
        ball.bounce_x()

    if ball.xcor()>360:
        l_score.scored()
        ball.set_default()
    elif ball.xcor()<-360:
        r_score.scored()
        ball.set_default()
screen.exitonclick()