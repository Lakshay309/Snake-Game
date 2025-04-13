from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score_board

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake=Snake()
food=Food()
score_board=Score_board()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on:bool=True
while(game_is_on):
    screen.update()
    time.sleep(0.1)

    snake.move()
    #  collision with food
    if snake.head.distance(food)<35:
        food.refresh()
        snake.extend()
        score_board.update_score()
    
    # Collision with wall
    if (snake.head.pos()[0]>290 or snake.head.pos()[0]<-290 or
        snake.head.pos()[1]>290 or snake.head.pos()[1]<-290):
        game_is_on=False
        score_board.game_over()
    
    # Detect tail collision 
    if snake.collision():
        game_is_on=False
        score_board.game_over()

screen.exitonclick() 