from turtle import Turtle, Screen

tim= Turtle()
screen=Screen()

#def move_forward():
#    tim.forward(10)
#screen.listen()
#screen.onkey(key="space",fun=move_forward) #pass function only name if function in another function
#screen.exitonclick()
heading=0
def counter_clockwise():
    global heading
    heading+=5
    tim.setheading(heading)

def clockwise():
    global heading
    heading -= 5
    tim.setheading(heading)
def move_forward():
    tim.forward(10)

def move_backwards():
    tim.forward(-10)
def clear_screen():
    tim.penup()
    tim.clear()
    tim.goto(0,0)
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c",fun=clear_screen)

screen.mainloop()