from turtle import Screen, Turtle
from player import Player
from car import Car
from scoreboard import Scoreboard
import random
import time

screen=Screen()
screen.tracer(0)
screen.setup(600,600)
screen.title("Cross the Road")



player=Player()
car=Car()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.go_up, "w")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    rand_number=random.randint(1,6)
    car.create_car(rand_number)
    car.move_cars()

    for cars in car.cars:
        if cars.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False
        print(cars.distance(player))

    if player.is_finish_line():
        player.start_pos()
        car.level_up()
        scoreboard.next_lvl()

screen.exitonclick()