from turtle import *
'''
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key='space',fun=move_forwards)
screen.exitonclick()
'''
#----------------------------------------------------
# Make an Etch-a-Sketch
# W - Forwards
# S - Backwards
# A - Counter -Clockwise
# D - Clockwise
# C = clear Drawing
'''
tim = Turtle()
screen =Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counter():
    new_heading = tim.heading() +10
    tim.setheading(new_heading)

def move_clockwise():
    new_heading=tim.heading() -10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen() # 이 명령어를 실행시켜야 키 입력모드가 실행되어 입력된 키에 반응한다.
screen.onkey(key='w',fun=move_forwards)
screen.onkey(key='s',fun=move_backwards)
screen.onkey(key='a',fun=move_counter)
screen.onkey(key='d',fun=move_clockwise)
screen.onkey(key='c',fun=clear)
exitonclick()
'''
#----------------------------------------------------------------------
# turtle racing project
from turtle import *
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle=[]
is_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_on = True

while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_on=False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You win! The {winning_turtle} turtle is the winner")
            else:
                print(f"You lose! The {winning_turtle} turtle is the winner")
        rand_move = random.randint(0, 10)
        turtle.forward(rand_move)



screen.exitonclick()






