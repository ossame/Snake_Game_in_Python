import turtle
from turtle import Turtle

MOVE_DISTANCE=20
up=90
down=270
left=180
right=0

class Snake:
    def __init__(self):
        self.pos = 0
        self.segments = []

        for i in range(0, 3):
            self.turtle = Turtle()
            self.turtle.shape("square")
            self.turtle.color("white")
            self.turtle.penup()
            self.turtle.goto(x=self.pos, y=0)
            self.pos = self.pos - 20
            self.segments.append(self.turtle)
        self.head = self.segments[0]


    def extend(self):
        self.turtle = Turtle()
        self.turtle.shape("square")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.goto(x=self.segments[-1].xcor(), y=self.segments[-1].ycor())
        self.segments.append(self.turtle)




    def move(self):

        for segment in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[segment - 1].xcor()
            y_pos = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x=x_pos, y=y_pos)
        self.head.forward(MOVE_DISTANCE)




    def up(self):
        if self.head.heading()!=up and self.head.heading() != down:
            self.segments[0].setheading(up)


    def down(self):
        if self.head.heading() != down and self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != left and self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != right and self.head.heading() != left :
            self.head.setheading(right)



