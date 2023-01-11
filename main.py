
'''
from turtle import *

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

# 점선 그리면서 나아가기

for i in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

'''

# 3 ~ 10각형 그리기
'''
import random
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeapSkyBlue", "LightSeaGreen","wheat","SlateGray","SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):

        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3,11):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)


#########################################################
for i in range(4):
    timmy.forward(100)
    timmy.right(90)
for i in range(5):
    timmy.forward(100)
    timmy.right(72)
for i in range(6):
    timmy.forward(100)
    timmy.right(60)
for i in range(8):
    timmy.forward(100)
    timmy.right(45)
'''

# -------------------------------------------------------
# 무작위 행보
'''
from turtle import *
import random
tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen","wheat","SlateGray","SeaGreen"]
directions= [0, 90 ,180, 270]
tim.pensize(10)
tim.speed("fastest")

for i in range(300):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colours))

'''
#-------------------------------------------------------------------------------------------
# 임의의 색상 RGB 생성하기
'''
from turtle import *
import random
t = Turtle()


colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

t.pensize(10)
t.speed("fastest")

directions= [0, 90 ,180, 270]
for i in range(100):
    t.color(random_color())
    t.forward(15)
    t.setheading(random.choice(directions))
'''


#-----------------------------------------------------------------
# 스피로그래프 그리기
'''
from turtle import *
import random
t = Turtle()
t.speed("fastest")
colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)



def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)

draw_spirograph(5)
'''
#----------------------------------------------------------------------------



