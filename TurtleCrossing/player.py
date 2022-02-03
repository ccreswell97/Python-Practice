from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape("turtle")
        self.setheading(90)
        self.reset_turtle()

    def hop_forward(self):
        self.forward(20)

    def hop_backward(self):
        self.backward(20)
    
    def reset_turtle(self):
        self.setpos(0,-275)