import turtle as t
import random
from turtle import Screen

john = t.Turtle()
john.pensize(1)
john.speed("fastest")
john.hideturtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)

    return random_color


def draw_circles():
    for _ in range(100):
        john.color(random_color())
        john.circle(100)
        john.left(360/100)


draw_circles()

screen = Screen()  # Instantiates the Screen() function.
screen.exitonclick()  # Sets the window to be closed by user.
