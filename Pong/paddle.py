from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, xpos, ypos):
        super().__init__()
        self.up()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(xpos, ypos)
    
    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)