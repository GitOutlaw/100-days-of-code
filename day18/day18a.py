import turtle as t
# from turtle import Screen
import random

tim = t.Turtle()

colors = ["light steel blue","forest green", "lawn green", "dark orchid", "firebrick","khaki","turquoise",
]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


# screen = Screen()
# screen.exitonclick()
