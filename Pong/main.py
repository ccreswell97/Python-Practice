from turtle import Screen, Turtle
from paddle import Paddle

def draw_court_lines():
    screen_lines = Turtle()
    screen_lines.speed("fastest")
    screen_lines.color("white")
    screen_lines.up()
    screen_lines.goto(-5, 295)
    screen_lines.setheading(270)
    screen_lines.hideturtle()

    for i in range(20):
        screen_lines.width(5)
        screen_lines.down()
        screen_lines.forward(10)
        screen_lines.up()
        screen_lines.forward(20)

def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("P O N G")
    screen.tracer(0)

    draw_court_lines()

    player_one_paddle = Paddle(350, 0)
    player_two_paddle = Paddle(-350, 0)
    screen.listen()
    screen.onkey(player_one_paddle.move_up, "Up")
    screen.onkey(player_one_paddle.move_down, "Down")

    screen.onkey(player_two_paddle.move_up, "w")
    screen.onkey(player_two_paddle.move_down, "s")
    
    game_is_on = True
    while game_is_on:
        screen.update()

    screen.exitonclick()

if __name__=="__main__":
    main()
