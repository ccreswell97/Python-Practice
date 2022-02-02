from turtle import Screen
from time import sleep
from player import Player
from car import Car

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Turtle Crossing")
    screen.tracer(0)

    # Make many cars run along the screen
    # Detect car/turtle collision
    # Create levels and detect end of crossing
    # Make cars move faster after level up

    player = Player()
    car = Car()

    screen.listen()
    screen.onkey(player.hop_forward, "w")
    screen.onkey(player.hop_backward, "s")

    game_is_on = True
    while game_is_on:
        screen.update()
        car.move_forward()
        sleep(0.1)
        
if __name__ == "__main__":
    main()