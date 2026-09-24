from turtle import Turtle

MOVE = 'True'
FONT = ("courier", 80, "normal")
ALIGNMENT = 'center'

class Score_board():
    def __init__(self):
        self.score = 0
    
    def create_L_score_board(self):
        self.board = Turtle()
        self.board.color('white')
        self.board.hideturtle()
        self.board.penup()
        self.board.goto(-50, 180)
        self.board.write(f"{self.score}", move= MOVE, align= ALIGNMENT, font= FONT)

    
    def create_R_score_board(self):
        self.board = Turtle()
        self.board.color('white')
        self.board.hideturtle()
        self.board.penup()
        self.board.goto(50,180)
        self.board.write(f"{self.score}", move= MOVE, align= ALIGNMENT, font= FONT)
