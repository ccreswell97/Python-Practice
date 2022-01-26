# Turtle racing game
# 

from turtle import Turtle, Screen
import random

def setup_turtles():
    colors = ["red", "yellow", "orange", "green", "blue", "indigo", "violet"]
    racers = []

    x = -230
    y = -100

    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color)
        y += 30
        new_turtle.goto(x, y)
        racers.append(new_turtle)

    return racers

def reset_turtles(turtles):
    x = -230
    y = -100

    for turtle in turtles:
        y += 30
        turtle.goto(x,y)
        
screen = Screen()
screen.setup(width=500, height=400)

play_again = True
times_played = 0


while play_again:
    is_race_on = False
    user_guess = screen.textinput("Make your guess", "Which turtle will win the race? Enter a color from the rainbow: ")

    if times_played == 0: racers = setup_turtles()

    if user_guess: is_race_on = True

    winner = ""
    while is_race_on:
        for turtle in racers:
            if turtle.xcor() > 230:
                is_race_on = False
                winner = turtle.pencolor()
            random_distance = random.randint(0, 30)
            turtle.forward(random_distance)

    writer = Turtle()
    writer.write(f"The winner is {winner}!", font=("Verdana", 20, "normal"), align="center")
    writer.hideturtle()

    play_again_input = screen.textinput("Make your choice", "Play again? (yes/no)").lower()    
    if play_again_input == "yes":
        writer.clear()
        reset_turtles(racers)
        times_played += 1
        play_again = True
    else:
        play_again = False
