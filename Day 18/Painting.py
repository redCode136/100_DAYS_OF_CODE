import colorgram
import turtle as t
import random

t.colormode(255)


def rgb_color():
    rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        rgb_colors.append(color.rgb)
    return rgb_colors

def draw_color():
    color=rgb_color()
    turtle=t.Turtle()
    ##set screen
    t.screensize(canvwidth=400, canvheight=400,
                 bg="white")
    width=-200
    height=-250
    turtle.penup()

    turtle.setposition(height,width)
    dot_size=20
    space=50
    turtle.pensize(dot_size)
    turtle.penup()



    for y in range(10):
        for x in range(10):
            turtle.dot(dot_size, random.choice(color))
            turtle.forward(space)
        width+=space
        turtle.setposition(-250, width)


draw_color()

t.exitonclick()
