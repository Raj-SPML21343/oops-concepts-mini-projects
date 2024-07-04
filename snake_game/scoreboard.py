from turtle import Turtle

# Define the file path
file_path = "High_score.txt"


def load_high_score(file_path):
    try:
        with open(file_path, "r") as file:
            high_score_str = file.read().strip()
            if high_score_str:
                return int(high_score_str)
            else:
                return 0  # Return 0 if the file is empty
    except FileNotFoundError:
        # Return a default value if the file doesn't exist
        return 0


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.high_score = load_high_score(file_path)
        self.refresh_score()

    def refresh_score(self):
        self.write(f"Score: {self.score}, High Score: {self.high_score}  ", align="center", font=('italic', 18, 'bold'))

    def increment_score(self):
        self.clear()
        self.score += 1
        self.refresh_score()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.save_high_score(file_path)
        self.home()  # equivalent to self.goto(0,0)
        self.write("GAME OVER ", align="center", font=('Ariel', 24, 'normal'))

    # Function to save the high score to a text file
    def save_high_score(self, file_path):
        with open(file_path, "w") as file:
            file.write(str(self.high_score))


