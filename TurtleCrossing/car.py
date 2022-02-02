from random import choice, randint
from turtle import Turtle

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.color(self.get_random_color())
        self.shape("square")
        self.setpos(290, randint(-100, 130))
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.x_move = 10

    def move_forward(self):
        x = self.xcor() - self.x_move
        self.setpos(x, self.ycor())

    def get_random_color(self):
        colors = ['green', 'blue', 'magenta', 'cyan', 'purple', 'orange']
        return choice(colors)