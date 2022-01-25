# This program re-creates the Damien Hirst spot paintings
# https://www.artsy.net/artist-series/damien-hirst-spots

import turtle
import random

colors = [(218, 156, 103), (30, 117, 139), (248, 243, 247), (189, 73, 37), (113, 173, 195), (17, 141, 111), (206, 148, 16), (54, 170, 127), (69, 24, 44), (80, 23, 12), (133, 181, 143), (116, 80, 120), (15, 176, 202), (2, 110, 102), (191, 149, 178), (128, 28, 10), (26, 59, 70), (228, 83, 32), (223, 206, 107), (108, 61, 4), (165, 97, 119), (46, 51, 48), (103, 32, 42), (125, 112, 170), (13, 88, 102), (167, 208, 200), (163, 207, 212), (188, 190, 197), (220, 178, 168), (203, 183, 196), (59, 63, 69)]

turtle.colormode(255)
ramona = turtle.Turtle()
ramona.width(10)
ramona.up()

x = -230
y = -130

ramona.setposition(x, y)

for row in range(8):
    for dot in range(11):
        dot_color = random.choice(colors)
        ramona.down()
        ramona.dot(dot_color)
        ramona.up()
        x += 45
        ramona.setx(x)
    x = -230
    y += 40
    ramona.setposition(x, y)


screen = turtle.Screen()
screen.exitonclick()
