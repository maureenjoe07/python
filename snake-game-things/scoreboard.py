from turtle import Turtle
MOVE = 'True'
FONT = ("courier", 15, "normal")
ALIGNMENT = 'center'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.update_score_borad()
        

             
    def increase_score(self):
        self.score += 1 
        self.clear()
        self.update_score_borad()

    def update_score_borad(self):
        self.goto(0,280)
        self.write(f"Score={self.score}", move= MOVE, align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg= 'Game over', move= MOVE, align= ALIGNMENT, font= FONT)
       
  
        