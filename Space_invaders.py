import turtle
import os

#set up the screen
w = turtle.Screen()
w.bgcolor("black")
w.title("Space Invaders")

#   draw bordrer
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lf(90)
border_pen.hideturtle()








