from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.shape("circle")
        self.color("white")
        self.speed("slow")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.setpos(x, y)
    
    def reset_position(self):
        self.home()
        self.x_axis_bounce()
        self.move_speed = 0.1
        
    def y_axis_bounce(self):
        self.y_move *= -1

    def x_axis_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9    