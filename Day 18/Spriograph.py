import turtle as t
import random


def draw_spirograph(size_gap):

    for x in range(int(360/size_gap)):
        turtle.circle(100)
        turtle.color(random_color())
        turtle.setheading(turtle.heading()+size_gap)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color=(r,g,b)
    return color

t.colormode(255)
turtle=t.Turtle()
turtle.speed(1000)
draw_spirograph(20)

t.exitonclick()
