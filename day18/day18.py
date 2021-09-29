import turtle as t
from turtle import Screen

tim = t.Turtle()
color1 = tim.color("blue")
color2 = tim.color("red")


########### Challenge 3 - Draw Shapes ########

# Triangle
tim.color("deep sky blue")
for _ in range(3):
    tim.right(120)
    tim.forward(100)

# Sqaure
tim.color("black")
for _ in range(4):
    tim.right(90)
    tim.forward(100)

# Pentagon
tim.color("dark violet")
for _ in range(5):
    tim.right(72)
    tim.forward(100)

# Hexagon
tim.color("saddle brown")
for _ in range(6):
    tim.right(60)
    tim.forward(100)

# Heptagon
tim.color("dark green")
for _ in range(7):
    tim.right(51.42)
    tim.forward(100)

# Octagon
tim.color("red")
for _ in range(8):
    tim.right(45)
    tim.forward(100)

# Nonagon
tim.color("dark turquoise")
for _ in range(9):
    tim.right(40)
    tim.forward(100)


# Decagon
tim.color("gold")
for _ in range(10):
    tim.right(36)
    tim.forward(100)


screen = Screen()
screen.exitonclick()
