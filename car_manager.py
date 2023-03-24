from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.goto(x_position)

    def move(self, speed):
        self.forward(speed)


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_y = random.randint(-250, 250)
        new_car = Car((300, random_y))
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.move(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
