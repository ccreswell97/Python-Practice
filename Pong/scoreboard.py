from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.player_score = 0
        self.xpos = xpos
        self.ypos = ypos
        self.update_scoreboard(xpos, ypos)

    def update_scoreboard(self, x, y):
        self.clear()
        self.goto(x,y)
        self.write(self.player_score, align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.player_score += 1
        self.update_scoreboard(self.xpos, self.ypos)