# PONG GAME.
from turtle import Turtle, Screen
from paddle import Paddle
from score_board import Score_board

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG GAME.')

mid_line = Turtle()
mid_line.hideturtle()
mid_line.pencolor('white')
mid_line.penup()
mid_line.goto(0, 290)
mid_line.setheading(-90)

paddle = Paddle()

paddle.create_left_paddle()
# paddle.create_right_paddle()

screen.listen()
screen.onkey(fun=paddle.move_up, key='Up')

# score_board = Score_board()
# score_board.create_L_score_board()
# score_board.create_R_score_board()


# draw = True
# while draw == True:
#     mid_line.pendown()
#     mid_line.speed('fastest')
#     mid_line.forward(10)
#     mid_line.penup()
#     mid_line.forward(10)

#     if mid_line.ycor() <= -290:
#         draw = False


# paddle.move_L_pad_up()

screen.exitonclick()