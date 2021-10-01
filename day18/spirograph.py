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


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        john.color(random_color())
        john.circle(100)
        john.setheading(john.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()  # Instantiates the Screen() function.
screen.exitonclick()  # Sets the window to be closed by user.
