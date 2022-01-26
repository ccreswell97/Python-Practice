from turtle import Turtle, Screen

def move_forward():
    ramona.forward(5)

def move_backward():
    ramona.backward(5)

def turn_left():
    ramona.left(10)

def turn_right():
    ramona.right(10)

def clear():
    ramona.clear()
    ramona.up
    ramona.setpos(0,0)

ramona = Turtle()
screen = Screen()

screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_right, "d")
screen.onkeypress(turn_left, "a")
screen.onkeypress(clear, "c")

screen.exitonclick()

