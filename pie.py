import turtle
from turtle import Screen
import random

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
          "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
john = turtle.Turtle()
john.width(6)
john.hideturtle()
john.speed('fastest')


def go(heading, step_size):
    john.setheading(heading)
    john.forward(step_size)


def random_walk(step_size, steps):
    # Assumes turtle.mode('standard')
    DIRECTIONS = (0, 90, 180, 270)
    for _ in range(steps):
        john.color(random.choice(colors))
        go(random.choice(DIRECTIONS), step_size)


random_walk(20, 100000)

screen = Screen()
screen.exitonclick()
