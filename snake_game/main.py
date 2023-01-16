from turtle import *
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
# 뱀게임-1 20일차
# Create a snake body
# Move the snake
# Control the snake

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        # is_on = False
        # scoreboard.game_over()


    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # is_on = False
            # scoreboard.game_over()


screen.exitonclick()








'''
x_position=[0,-20,-40]
for i in range(3):
    t = Turtle(shape="square")
    t.fillcolor("white")
    t.pencolor("white")
    t.penup()
    t.goto(x_position[i],0)

'''
