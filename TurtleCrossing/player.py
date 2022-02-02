from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape("turtle")
        self.setheading(90)
        self.setpos(0,-275)

    def hop_forward(self):
        self.forward(20)

    def hop_backward(self):
        self.backward(20)