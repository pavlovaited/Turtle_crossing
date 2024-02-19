import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()

    # detecting collision with cars:
    for cars in car_manager.all_cars:
        if player.distance(cars) < 20:
            scoreboard.game_over()
            game_is_on = False
            screen.exitonclick()

    # detect winning a point
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.reset_position()
        car_manager.increase_speed()
