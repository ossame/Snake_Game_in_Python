import timeit
import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen=Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)


snake=Snake()
food=Food()
score_board=ScoreBoard()


####
frame_count = 0
# start_time = time.time()
####

screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)

game_on=True
score_board.show_score()



start_time = timeit.default_timer()

while game_on:
    screen.update()
    xpo = snake.head.xcor()
    ypo = snake.head.ycor()
    time.sleep(0.0166)

    # FPS calculation
    frame_count += 1

    elapsed_time = timeit.default_timer() - start_time
    if elapsed_time >= 1.0:
        fps = frame_count
        print(frame_count)
        turtle.goto(x=-270, y=270)
        turtle.pencolor("red")
        turtle.clear()
        turtle.write(f"FPS: {fps:.2f}")
        print(f"FPS: {fps:.2f}")
        start_time = timeit.default_timer()
        fps = 0
        frame_count = 0


    if xpo==280 or xpo==-280 or ypo==280 or ypo==-280:
        score_board.game_over()
        game_on=False

    for i in  range(1, len(snake.segments)):
        if snake.head.distance(snake.segments[i])<10:
            score_board.game_over()
            game_on=False


    snake.move()



    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score_board.refresh()
        score_board.show_score()

































screen.exitonclick()