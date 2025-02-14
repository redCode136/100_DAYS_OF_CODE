from turtle import  Turtle ,Screen

point= Turtle()
screen= Screen()

color=["green","red","yellow","blue","purple","black","brown"]
def draw_shape():
    grad=360
    seiten=3
    for x in color:
        for y in range(seiten):
            point.forward(100)
            point.left(grad/seiten)
        point.color(x)
        seiten+=1


draw_shape()
screen.exitonclick()