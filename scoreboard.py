from turtle import Turtle
from turtle import Screen


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0

    def show_score(self):
        self.goto(x=0, y=270)
        self.pencolor("white")
        self.penup()
        self.write(f"score: {self.score}", align="center", font="normal")
        self.hideturtle()

    def game_over(self):
        self.goto(x=-50, y=10)
        self.penup()
        self.pencolor("red")
        self.write("GAME OVER" , font="arial")
    def refresh(self):
        self.score+=1
        self.clear()


