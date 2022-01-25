import turtle
from generate_random_color import generate_random_color

def draw_many_shapes():
    for i in range(3, 11):
        turn_degree = 360/i
        ramona.pencolor(generate_random_color())
        for j in range(i):
            ramona.forward(100)
            ramona.left(turn_degree)


ramona = turtle.Turtle()
ramona.shape("turtle")
turtle.colormode(255)

draw_many_shapes()

screen = turtle.Screen()
screen.exitonclick()