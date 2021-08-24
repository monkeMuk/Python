import turtle
import os
from random import choice, randint
#Version 1, no OOP implemented

window = turtle.Screen()
window.title("Classic Pong")
window.bgcolor("black")
window.setup(width = 800,height = 600)
window.tracer(0)    #Stops the window from updating

#   Score
score_a = 0
score_b = 0


#   Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

#   Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)

#   Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

speedX = choice([i for i in range(-2,2)if i not in [-1,0,1]])
DirectionY = randint(-2,2)

ball.dx = speedX
ball.dy = DirectionY

#   Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  |   Player B: 0", align = "center", font=("Coureier",24,"normal"))


#   Function

paddles = [paddle_a,paddle_b]

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#   Keyboard binding

#   Paddle a
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
#   Paddle b
window.onkeypress(paddle_b_up, "8")
window.onkeypress(paddle_b_down, "2")

#   main game loop
while True:
    window.update()
    #   ball movements
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #   Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay Pong_bounce.wav&")

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  |   Player B: {}".format(score_a, score_b), align = "center", font=("Coureier",24,"normal"))

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  |   Player B: {}".format(score_a, score_b), align = "center", font=("Coureier",24,"normal"))


    
    #   Paddle and Ball collission
    if (ball.xcor() > 340 and ball.xcor()< 350) and (ball.ycor()< paddle_b.ycor()
    + 40 and ball.ycor()> paddle_b.ycor()- 40 ):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor()> -350) and (ball.ycor()< paddle_a.ycor()
    + 40 and ball.ycor()> paddle_a.ycor()- 40 ):
        ball.setx(-340)
        ball.dx *= -1


    
    

