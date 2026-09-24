from turtle import Turtle

LEFT_POSITION = (375, 0)
RIGHT_POSITION = (-375, 0)

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=7, stretch_len= 1,outline= 8)

    def create_left_paddle(self):
        self.goto(LEFT_POSITION)
 
    def create_right_paddle(self):
        self.goto(RIGHT_POSITION)
    
    def move_up(self):
        new_y = self.ycor() + 20
        self.setheading(self.xcor(), new_y)
   
