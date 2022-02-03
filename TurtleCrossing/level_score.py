from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier", 20, "normal")

class LevelScore(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.up()
        self.setpos(-230, 270)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)