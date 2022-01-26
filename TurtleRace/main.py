# Turtle racing game
# Choose a turtle to bet on and try to double your money

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
money = 100

writer = Turtle()
money_writer = Turtle()
money_writer.hideturtle()
money_writer.up()
money_writer.setpos(-240, 180)
money_writer.write(f"Money: ")

while play_again:
    is_race_on = False
    if times_played == 0: racers = setup_turtles()
    
    writer.hideturtle()
    writer.up()
    writer.setpos(-210, 180)
    writer.write(f"${money}")
    
    user_guess = screen.textinput("Make your guess", "Which turtle will win the race? Enter a color from the rainbow.").lower()
    user_bet = int(screen.numinput("Make your bet", f"You have ${money}, how much would you like to bet?"))
    while user_bet > money:
        user_bet = int(screen.numinput("Make your bet", f"Oops. That's more than you have. You have ${money}, how much would you like to bet?"))    
    
    money -= user_bet

    if user_guess: is_race_on = True

    winner = ""
    while is_race_on:
        for turtle in racers:
            if turtle.xcor() > 230:
                is_race_on = False
                winner = turtle.pencolor()
            random_distance = random.randint(0, 30)
            turtle.forward(random_distance)

    writer.home()
    writer.write(f"The winner is {winner}!", font=("Verdana", 20, "normal"), align="center")

    if winner == user_guess:
        money += user_bet*2

    if money > 0:
        play_again_input = screen.textinput("Make your choice", f"The winner was {winner}. Play again? (yes/no)").lower()    
        if play_again_input == "yes":
            writer.clear()
            reset_turtles(racers)
            times_played += 1
            play_again = True
        else:
            play_again = False
    else:
        writer.clear()
        writer.write("You are out of money, click to exit",  font=("Verdana", 20, "normal"), align="center")
        screen.exitonclick()
        play_again = False
