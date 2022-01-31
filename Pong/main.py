from turtle import Screen, Turtle
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
from time import sleep

def draw_court_lines():
    screen_lines = Turtle()
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

    right_player_paddle = Paddle(350, 0)
    left_player_paddle = Paddle(-350, 0)
    ball = Ball()
    left_scoreboard = Scoreboard(-100, 200)
    right_scoreboard = Scoreboard(100, 200)

    screen.listen()
    screen.onkey(right_player_paddle.move_up, "Up")
    screen.onkey(right_player_paddle.move_down, "Down")

    screen.onkey(left_player_paddle.move_up, "w")
    screen.onkey(left_player_paddle.move_down, "s")
    
    game_is_on = True
    sleep_value = 0.1
    while game_is_on:
        screen.update()
        ball.move()
        sleep(ball.move_speed)

        # top wall collision
        if (ball.ycor() < -280 or ball.ycor() > 280):
            # bounce off wall
            ball.y_axis_bounce()
        
        # paddle collision
        if (ball.distance(right_player_paddle) < 60 and ball.xcor() > 320 or ball.distance(left_player_paddle) < 60 and ball.xcor() < -320):
            ball.x_axis_bounce()
        
        # wall behind paddle collision (out of bounds)
        if (ball.xcor() < -380):
            ball.reset_position()
            right_scoreboard.add_point()
        
        if (ball.xcor() > 380):
            ball.reset_position()
            left_scoreboard.add_point()

    screen.exitonclick()

if __name__=="__main__":
    main()
