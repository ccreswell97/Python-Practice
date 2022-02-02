from turtle import Screen
from time import sleep
from player import Player
from car_manager import CarManager

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Turtle Crossing")
    screen.tracer(0)

    # TODO: Detect car/turtle collision
    # TODO: Create levels and detect end of crossing
    # TODO: Make cars move faster after level up

    player = Player()
    car_manager = CarManager()

    screen.listen()
    screen.onkey(player.hop_forward, "w")
    screen.onkey(player.hop_backward, "s")

    game_is_on = True
    while game_is_on:
        sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()
        
        
if __name__ == "__main__":
    main()