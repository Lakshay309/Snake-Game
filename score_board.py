from turtle import Turtle

ALIGNMENT="center"
FONT=("Courier",24,"normal")
MOVE=False

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,266)
        self.display_score()


    def display_score(self):
        score="Score: "+str(self.score)
        self.write(arg=score,move=MOVE,align=ALIGNMENT,font=FONT)

    def update_score(self):
        self.score+=1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.color("pink")
        self.write(arg="GAME OVER",move=MOVE,align=ALIGNMENT,font=FONT)