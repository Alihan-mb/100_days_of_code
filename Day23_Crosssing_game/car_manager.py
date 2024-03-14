from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def increase_speed():
    global STARTING_MOVE_DISTANCE
    STARTING_MOVE_DISTANCE += MOVE_INCREMENT


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 2:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            random_y = random.randint(-230, 230)
            new_car.goto(x=300, y=random_y)
            self.cars.append(new_car)

    def moving_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def car_to_check(self):
        for car in self.cars:
            return car
