import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# create player, car and scoreboard object
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# detect key presses
screen.listen()
screen.onkey(key="Up", fun=player.move)

loop_count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # generate car every 6th iteration
    if loop_count % 6 == 0:
        car_manager.generate_car()

    # move cars
    car_manager.move_cars()

    # remove cars that are off-screen and detect collision with player
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
        if car.xcor() < -400:
            car_manager.cars.remove(car)

    # Detect if player has reached on top of the screen
    if player.ycor() > 280:
        player.player_reset()
        scoreboard.increase_level()
        car_manager.increase_speed()

    loop_count += 1
    screen.delay(100)

screen.exitonclick()
