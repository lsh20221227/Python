from turtle import *
from snake import Snake
import time
# 뱀게임-1 20일차
# Create a snake body
# Move the snake
# Control the snake

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


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
