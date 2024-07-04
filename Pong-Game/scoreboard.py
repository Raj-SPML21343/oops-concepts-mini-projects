from turtle import Turtle
import time

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        time.sleep(0.001)
        self.goto(x=-150, y=220)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(x=150, y=220)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()
