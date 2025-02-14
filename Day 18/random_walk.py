import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color=(r,g,b)
    return color

t.colormode(255)
turtle=t.Turtle()
turtle.speed(10)
turtle.pensize(5)
directions = [0, 90, 180, 270]

for x in range(5000):
    direction = random.choice(directions)
    turtle.forward(50)
    turtle.setheading(direction)
    turtle.color(random_color())
