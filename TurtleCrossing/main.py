from turtle import Screen
from time import sleep
from player import Player
from car_manager import CarManager
from level_score import LevelScore

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Turtle Crossing")
    screen.tracer(0)
    
    player = Player()
    car_manager = CarManager()
    level_score = LevelScore()

    screen.listen()
    screen.onkey(player.hop_forward, "w")
    screen.onkey(player.hop_backward, "s")

    game_is_on = True
    while game_is_on:
        sleep(0.1)
        screen.update()

        # Detect end of level 
        if player.ycor() > 220:
            level_score.increase_score()
            player.reset_turtle()
            car_manager.increase_car_speed()

        # TODO: Detect car/turtle collision

        car_manager.create_car()
        car_manager.move_cars()
        
        
if __name__ == "__main__":
    main()