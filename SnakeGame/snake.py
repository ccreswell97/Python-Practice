from turtle import Turtle, Screen

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        y = 0
        for i in range(3):
            self.add_segment((x,y))
            x -= 20
    
    def move(self):
        for s in range(len(self.segments) - 1, 0, -1):
            x = self.segments[s-1].xcor()
            y = self.segments[s-1].ycor()
            self.segments[s].goto(x,y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.up()
        segment.goto(position)
        self.segments.append(segment)