from turtle import Turtle
class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("high_scores.txt") as file:
            self.highscore=int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.highscore}", False, "center", ("Britannic Bold",20,"normal"))

    def increment_score(self):
        self.score+=1
        self.update()

    def game_over(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("high_scores.txt",mode="w") as file:
                file.write(str(self.highscore))
        self.update()
        self.goto(0,0)
        self.write("GAME OVER",False,"center",("arial",15,"normal"))

