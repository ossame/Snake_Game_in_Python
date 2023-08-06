import turtle
import time

class Fps:
    def __init__(self):
        # Set up the screen
        self.screen = turtle.Screen()
        self.screen.title("FPS Display")

        # Set up the turtle for FPS display
        self.fps_pen = turtle.Turtle()
        self.fps_pen.hideturtle()
        self.fps_pen.penup()
        self.fps_pen.goto(x=-250, y=250)
        self.fps_pen.color("red")

    def calculate_fps(self, frame_time):
        fps = 1.0 / frame_time
        self.fps_pen.clear()
        self.fps_pen.write(f"FPS: {fps:.2f}", align="left", font=("Arial", 16, "normal"))

    def run(self):
        previous_time = time.time()
        time.sleep(0.00001)

        # Your game logic and rendering code here

        # Calculate frame time
        current_time = time.time()
        frame_time = current_time - previous_time
        previous_time = current_time
        previous_time = current_time

        # Calculate and display FPS
        if frame_time > 0:
            self.calculate_fps(frame_time)

        # Update the screen
        self.screen.update()



