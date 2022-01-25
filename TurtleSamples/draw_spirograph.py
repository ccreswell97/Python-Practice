import turtle
from generate_random_color import generate_random_color

def draw_spirograph(circle_radius, size_of_gap):
    for i in range(int(360 / size_of_gap)):
        ramona.color(generate_random_color())
        ramona.circle(circle_radius)
        ramona.setheading(ramona.heading() + size_of_gap)

ramona = turtle.Turtle()
turtle.colormode(255)
ramona.shape("turtle")
ramona.speed("fastest")

draw_spirograph(75, 5)

screen = turtle.Screen()
screen.exitonclick()