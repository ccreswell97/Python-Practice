import turtle

def draw_square(side_length):
    for i in range(4):
        ramona.forward(side_length)
        ramona.left(90) 

ramona = turtle.Turtle()
ramona.shape("turtle")

draw_square(100)

screen = turtle.Screen()
screen.exitonclick()