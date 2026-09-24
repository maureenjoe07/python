from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(False)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(key='Up', fun= snake.UP)
screen.onkey(key='Down', fun= snake.DOWN)
screen.onkey(key='Left', fun= snake.LEFT)
screen.onkey(key='Right', fun= snake.RIGHT)

game_on = True
while game_on == True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.regenerate()
        scoreboard.increase_score()
        scoreboard.update_score_borad()
        snake.extend()

    if snake.head.xcor() >= 299.5 or snake.head.xcor() <= -299.5 or snake.head.ycor() >= 299.5 or snake.head.ycor() <= -299.5:
        game_on = False
        scoreboard.game_over()

    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
         

screen.exitonclick()
 
