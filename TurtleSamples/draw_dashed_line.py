import turtle

def draw_dashed_line(number_of_dashes):
    for i in range(number_of_dashes):
        ramona.forward(10)
        ramona.up()
        ramona.forward(10)
        ramona.down()

ramona = turtle.Turtle()
ramona.shape("turtle")

draw_dashed_line(10)

screen = turtle.Screen()
screen.exitonclick()