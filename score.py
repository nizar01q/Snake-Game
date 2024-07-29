from turtle import Turtle

ALIGNMENT = "center"
FONT = ('courier', 20, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.high_score = self.read_txt()
        self.color("whitesmoke")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def read_txt(self):
        with open("data.txt") as file:
            return int(file.read())

    def write_txt(self,w):
        with open("data.txt", mode="w") as file:
            (file.write(w))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.user_score}  High Score: {self.high_score} ", align=ALIGNMENT, font=FONT)
        self.write_txt(str(self.high_score))

    def reset_score(self):
        if self.user_score > self.high_score:
            self.high_score = self.user_score
        self.user_score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.user_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", align=ALIGNMENT, font=('courier', 50, 'bold'))




