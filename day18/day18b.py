import turtle as t
import random
from turtle import Screen

# Sets the parameters for the turtle object.
john = t.Turtle()
john.pensize(6)
john.hideturtle()
john.speed('fastest')

# List used to select random color.
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
          "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# Sets direction east, north, west & south.
DIRECTIONS = [0, 90, 180, 270]

for _ in range(200):
    john.color(random.choice(colors)) # Chooses random color.
    john.setheading(random.choice(DIRECTIONS)) # Chooses random direction.
    john.forward(10) # Moves the turtle forward.

screen = Screen() # Instantiates the Screen() function.
screen.exitonclick() # Sets the window to be closed by user pressing close.
