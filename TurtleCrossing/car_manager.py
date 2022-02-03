from random import choice, randint 
from turtle import Turtle

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.random_choices = [0]

    def create_car(self):
        random_chance = randint(0,6)
        if random_chance in self.random_choices:
            new_car = Turtle("square")
            new_car.up()
            new_car.color(self.get_random_color())
            new_car.setpos(290, randint(-200, 200))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def get_random_color(self):
        colors = ['green', 'blue', 'magenta', 'cyan', 'purple', 'orange']
        return choice(colors)
    
    def increase_car_speed(self):
        self.move_distance += 5
        if self.move_distance >= 15:
            self.increase_random_chance()

    def increase_random_chance(self):
        if len(self.random_choices) < 7:
            last_element = self.random_choices[-1]
            self.random_choices.append(last_element + 1)