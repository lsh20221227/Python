

#-----------------------------------------------------------------------------------------------------------------------
from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time



# Create the screen
turtle=Turtle()
screen=Screen()
ball = Ball()
scoreboard = ScoreBoard()


screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))



screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) <50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()

#------------------------------------------------------------------------------
# 스스로 게임 구조 만들어보고 비교해보기
# 전체 테이블/경계선 만들기
# 유저 2명의 패들만들기
# 패들 움직이기
# 공 만들기
# 공 움직이기
# 점수판 만들기
# 점수 획득 조건 만들기
# 최종 결과