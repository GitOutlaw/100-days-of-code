import turtle as t
import random
from turtle import Screen


john = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)

    return random_color
    

# Tuple with directions east, north, west & south represented numerically.
DIRECTIONS = (0, 90, 180, 270)

john.pensize(8)
john.hideturtle()
john.speed('fastest')

for _ in range(200):    
    john.color(random_color())  # Chooses random color.
    john.setheading(random.choice(DIRECTIONS))  # Chooses random direction.
    john.forward(10)  # Moves the turtle forward.

screen = Screen()  # Instantiates the Screen() function.
screen.exitonclick()  # Sets the window to be closed by user pressing close.
