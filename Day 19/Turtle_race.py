import turtle
from turtle import Turtle,Screen
import random

is_race_on=False
screen=Screen()
screen.setup(height=400,width=500)
user_bet=screen.textinput(title="Hallo",prompt="Which Turtle wins the race and Enter a color:")
color=["red","green","yellow","blue","purple","brown"]
all_turtle=[]

pos=[-150,-100,-50,50,100,150]
for x in range(0,6):
    new_turtle= Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(-150,pos[x])
    new_turtle.color(color[x])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        move_distance = random.randint(0, 10)
        turtle.forward(move_distance)
        winning_color=turtle.pencolor()
        if turtle.xcor()>230:
            is_race_on=False
            winning_color = turtle.pencolor()
            print(turtle.color())
            if winning_color==user_bet:
                print(f"you won. The {winning_color} turtle is the winner")
            else:
                print(f"you LOST! The {winning_color} turtle is the winner")
            break


screen.exitonclick()