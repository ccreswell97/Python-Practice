from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("green")
        self.speed("fastest")
        self.goto(randint(-280, 280), randint(-280, 280))

    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))