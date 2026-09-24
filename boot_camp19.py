from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=500)
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "orange", "purple", "yellow"]
y_axis = [150, 100, 50, 0, -50, -100]
list_of_turtles = []

for obj in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[obj])
    new_turtle.penup()
    new_turtle.goto(x=-280, y= y_axis[obj]) 
    list_of_turtles.append(new_turtle)

start_race = True
while start_race == True:
    for turtle in list_of_turtles:
        motion = random.randint(0, 10)
        turtle.forward(motion)

        if turtle.xcor() >= 290:
            start_race = False
            winner = turtle.pencolor()
            print(winner)

if user_choice == winner:
    print(f'You win. The {winner} turtle won.')
else:
    print(f'You lose. The {winner} turtle won.')
   
   



# def move_f():
#     tim.forward(10)

# def move_b():
#     tim.backward(10)

# def move_l():
#     tim.left(10)

# def move_r():
#     tim.right(10)

# def restart():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkeypress(key= "W", fun= move_f)
# screen.onkeypress(key= "S", fun= move_b)
# screen.onkeypress(key= "A", fun= move_l)
# screen.onkeypress(key= "D", fun= move_r)
# screen.onkeypress(key= "space", fun= restart)




screen.exitonclick()