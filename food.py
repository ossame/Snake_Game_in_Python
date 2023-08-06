from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        xpos=random.randint(-290, 290)
        ypos=random.randint(-290, 290)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed(0)
        self.goto(x=xpos, y=ypos)
    def refresh(self):
        xpos = random.randint(-280, 280)
        ypos = random.randint(-280, 280)
        self.goto(x=xpos, y=ypos)






