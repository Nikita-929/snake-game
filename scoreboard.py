from turtle import Turtle
from datetime import datetime
import os

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.txt")
LOG_FILE = os.path.join(os.path.dirname(__file__), "score_log.txt")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open(DATA_FILE, mode="r") as data:
                self.high_score = int(data.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

        # Show restart hint below
        self.goto(0, -40)
        self.write("Press R to Restart", align=ALIGNMENT, font=("Courier", 16, "normal"))

        # Save score with timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, mode="a") as log_file:
            log_file.write(f"{timestamp} - Score: {self.score}\n")

        # Save high score if needed
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA_FILE, mode="w") as data:
                data.write(f"{self.high_score}")
