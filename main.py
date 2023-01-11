# DAY 18
from colorgram import *

'''
rgb_colors = []
colors=colorgram.extract('image.jpg',30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)
'''

#[(234, 222, 113), (28, 109, 184), (225, 61, 90), (224, 151, 90), (124, 153, 205), (215, 130, 162), (139, 89, 52), (38, 194, 107), (105, 108, 190), (140, 177, 27), (240, 155, 184), (186, 48, 80), (109, 192, 156), (224, 63, 55), (186, 18, 37), (20, 182, 210), (146, 221, 172), (39, 53, 115), (136, 217, 230), (239, 172, 157), (176, 174, 227), (25, 149, 113), (36, 36, 69), (187, 218, 9), (76, 28, 33), (75, 35, 29)]


##########################################
'''
colors=colorgram.extract('image.jpg',30)
#print(colors)
#first_color = colors[0]
#rgb=first_color.rgb
#print(rgb)

def extract_color(a):
    """parameter is colorgram.extract('image.jpg',6)"""
    image_color=[]
    for i in a:
        rgb=i.rgb
        r=rgb[0]
        g=rgb[1]
        b=rgb[2]
        image_color.append((r,g,b))
    return image_color


rgb=extract_color(colors)
print(rgb)
'''
#-----------------------------------------------------------------------------------------
# 스팟 페인팅 프로젝트
# 점의 크기는 약 20, 점들의 간격은 약 50
# 구글에서 다운받은 이미지 추출한 색상 중에 255에 가까운 (흰색) 색상들은 지우고 시작

#from turtle import *
#import random

color_list=[(234, 222, 113), (28, 109, 184), (225, 61, 90), (224, 151, 90), (124, 153, 205), (215, 130, 162), (139, 89, 52), (38, 194, 107), (105, 108, 190), (140, 177, 27), (240, 155, 184), (186, 48, 80), (109, 192, 156), (224, 63, 55), (186, 18, 37), (20, 182, 210), (146, 221, 172), (39, 53, 115), (136, 217, 230), (239, 172, 157), (176, 174, 227), (25, 149, 113), (36, 36, 69), (187, 218, 9), (76, 28, 33), (75, 35, 29)]

#-----------------------------------------------------------------------------------
# SOLUTION

import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle() #화살표 숨기기

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



############################################################################################################
'''
t = Turtle()

t.speed("fastest")
colormode(255)



def circle_position(x,y):
    t.penup()
    t.setposition(x,y)
    t.pendown()



def draw_circle():
    for i in range(10):
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.penup()
        t.forward(50)
        t.pendown()
        t.color(random.choice(color_list))

x=-300
y=-300
for i in range(10):
    circle_position(x,y)

    draw_circle()
    t.setheading(90)
    t.penup()
    t.forward(50)
    t.pendown()
    t.setheading(0)
    y+=50

exitonclick()
'''

##########################################################################################







