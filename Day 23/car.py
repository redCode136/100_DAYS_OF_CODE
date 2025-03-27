from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class Car():
    def __init__(self):
        self.cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self, gen_value):
        if gen_value==1:
            new_car=Turtle()
            new_car.penup()
            new_car.shapesize(1, 2)

            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.goto(350,random.randint(-200,200))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            new_xcor=car.xcor()-self.car_speed
            car.goto(new_xcor,car.ycor())


    def level_up(self):
        self.car_speed+=MOVE_INCREMENT