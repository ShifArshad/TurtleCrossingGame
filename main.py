import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.refresh()
        score.level_up()
        car.speed_increase()



screen.exitonclick()