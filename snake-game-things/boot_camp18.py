#TURTLR GRAPHICS, TUPLES AND IMPORTING MODULES.
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(1.0, 1.0)
screen.colormode(255)

Betty = Turtle()
Betty.shape('turtle')
Betty.color('green')
# for i in range(4):
#     Betty.forward(100)
#     Betty.left(90)

# for i in range(10):
#     Betty.pendown()
#     Betty.forward(10)
#     Betty.penup()
#     Betty.forward(10)

# def triangle():
#     for i in range(3):
#         Betty.forward(100)
#         Betty.right(120)

# def square():
#     for i in range(4):
#         Betty.forward(100)
#         Betty.right(90)

# def pentagon():
#     for i in range(5):
#         Betty.forward(100)
#         Betty.right(72)
       
# def hexagon():
#     for i in range(6):
#         Betty.forward(100)
#         Betty.right(60)

# def heptagon():
#     for i in range(7):
#         Betty.forward(100)
#         Betty.right(52)

# def octagon():
#     for i in range(8):
#         Betty.forward(100)
#         Betty.right(45)

# def nonagon():
#     for i in range(9):
#         Betty.forward(100)
#         Betty.right(40)

# def decagon():
#     for i in range(10):
#         Betty.forward(100)
#         Betty.right(36)

# triangle()
# square()
# pentagon()
# hexagon()
# octagon()
# nonagon()
# decagon()

# for j in range(3, 11):
#     num_of_sides = j
#     angle = (360 / num_of_sides)
#     for i in range(num_of_sides):
#             Betty.forward(100)
#             Betty.right(angle)


colours = ["red", "blue", "green", "yellow", "black", "cyan", "magenta", "navy", "skyblue", "turquoise", "azure", "cadet blue", "aquamarine", "chocolate"]
directions = [0, 90, 180, 270]
Betty.pensize(15)
Betty.speed("fast")


def random_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    color = (red, blue, green)
    return color


# for i in range(200):
#     Betty.pencolor(random_color())
#     Betty.forward(random.randint(50, 80))
#     Betty.setheading(random.choice(directions))

# for i in range(75):
#     Betty.speed("fastest")
#     Betty.pencolor(random_color())
#     Betty.circle(100)
#     Betty.left(5)


n = 0
for j in range(10):
    for i in range(10):
        Betty.penup()
        Betty.dot(20, random_color())
        Betty.forward(30)
   
    Betty.setposition(0, n+25)
    n += 25



screen.exitonclick()
