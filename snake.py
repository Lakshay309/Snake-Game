from turtle import Turtle

MOVE_SPEED:int=20
STARTING_POSITIONS:list[tuple]=[(0,0),(-20,0),(-40,0)]
RIGHT:int=0
UP:int=90
LEFT:int=180
DOWN:int=270

# Create a snake class
class Snake:
    def __init__(self):
        self.segments:list[Turtle]=[]
        self.create_snake()
        self.head=self.segments[0]
    
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)    
    
    def add_segment(self,pos:tuple):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(pos)
        self.segments.append(new_segment)

    def move(self):
        segments=self.segments
        for i in range(len(segments)-1,-1,-1):
            if(i==0):
                segments[i].forward(MOVE_SPEED)
            else:
                segments[i].setposition(segments[i-1].pos())

    def up(self):
        if(self.head.heading()!=UP and self.head.heading()!=DOWN):
            self.head.setheading(UP)

    def down(self):
        if(self.head.heading()!=DOWN and self.head.heading()!=UP):
            self.head.setheading(DOWN)

    def left(self):
        if(self.head.heading()!=LEFT and self.head.heading()!=RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if(self.head.heading()!=RIGHT and self.head.heading()!=LEFT):
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.segments[-1].pos())
    
    def collision(self)->bool:
        head=self.head
        for pos in self.segments[1:]:
            if head.distance(pos)<10:
                return True
        return False