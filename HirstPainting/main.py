from turtle import Screen, Turtle
import random

def draw_square(side_length):
    for i in range(4):
        ramona.forward(side_length)
        ramona.left(90) 

def draw_dashed_line(number_of_dashes):
    for i in range(number_of_dashes):
        ramona.forward(10)
        ramona.up()
        ramona.forward(10)
        ramona.down()

def draw_many_shapes():
    colors = ["red", "pink", "blue", "green", "brown", "black", "cyan", "magenta", "orange", "purple"]
    for i in range(3, 11):
        turn_degree = 360/i
        ramona.pencolor(random.choice(colors))
        for j in range(i):
            ramona.forward(100)
            ramona.left(turn_degree)

ramona = Turtle()
ramona.shape("turtle")


#draw_square(100)
#draw_dashed_line(5)
draw_many_shapes()

screen = Screen()
screen.exitonclick()