from random import choice, randint
from turtle import Turtle

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.up()
            new_car.color(self.get_random_color())
            new_car.setpos(290, randint(-200, 200))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def get_random_color(self):
        colors = ['green', 'blue', 'magenta', 'cyan', 'purple', 'orange']
        return choice(colors)