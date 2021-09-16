import turtle
import time
from random import randint  

d = 0.1
score = 0
high_score = 0

#   setup screen
w = turtle.Screen()
w.title("Snake")
w.bgcolor("black")
w.setup(width = 600, height = 600)
w.tracer(0) #turns off screen updates

#   snake head
Snake_head = turtle.Turtle()
Snake_head.speed(0) #animation speed of the turtle module/ fastest animation speed
Snake_head.shape("square")
Snake_head.color("green")
Snake_head.penup() #turtle module acts like a pen, this prevents it from drawing anything
Snake_head.goto(0,0)
Snake_head.direction = "stop"

#   Snake food
food = turtle.Turtle()
food.speed(0) 
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

square = []

#   Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle() #  Hides the turtle
pen.goto(0,260)
pen.write("Score    |   High Score    |",align ="center", font = ("courier",24,"normal" ))



#   Functions
def go_up():
    if Snake_head.direction != "down":
        Snake_head.direction = "up"

def go_down():
    if Snake_head.direction != "up":
        Snake_head.direction = "down"

def go_left():
    if Snake_head.direction != "right":
        Snake_head.direction = "left"

def go_right():
    if Snake_head.direction != "left":
        Snake_head.direction = "right"



def move():
    if Snake_head.direction == "up":
        y = Snake_head.ycor()
        Snake_head.sety(y + 20)

    if Snake_head.direction == "down":
        y = Snake_head.ycor()
        Snake_head.sety(y - 20)

    if Snake_head.direction == "right":
        x = Snake_head.xcor()
        Snake_head.setx(x + 20)

    if Snake_head.direction == "left":
        x = Snake_head.xcor()
        Snake_head.setx(x - 20)

#   Keyboard binding 
w.listen()
w.onkeypress(go_up, "w")
w.onkeypress(go_down, "s")
w.onkeypress(go_left, "a")
w.onkeypress(go_right, "d")

#   Main game loop
while True:
    w.update()
    #   Check for border collision
    if Snake_head.xcor() > 290 or Snake_head.xcor()< -290 or Snake_head.ycor() > 290 or Snake_head.ycor()< -290:
        time.sleep(1)
        Snake_head.goto(0,0)
        Snake_head.direction = "stop"

    #   move food to another location
    if Snake_head.distance(food) < 20:
        #   Moves the food to a random spot
        x = randint(-290,290)
        y = randint(-290,290)
        food.goto(x,y)

        #   Add a square
        Newsquare = turtle.Turtle()
        Newsquare.speed(0)
        Newsquare.shape("square")
        Newsquare.color("light green")
        Newsquare.penup()
        square.append(Newsquare)

        #   Score system
        score += 1
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write(f"Score   {score}|   High Score    {high_score}|",align ="center", font = ("courier",24,"normal" ))

    
        #   Move the end square first in reverse order
    for i in range(len(square)-1,0,-1):
        x = square[i - 1].xcor()
        y = square[i - 1].ycor()
        square[i].goto(x,y)
            #   still dont get it
        
        #   Move segment 0 where the head is
    if len(square)> 0:
        x = Snake_head.xcor()
        y = Snake_head.ycor()
        square[0].goto(x,y)

    move()

    #   Check head collision with body
    for s in square:
        if s.distance(Snake_head) < 20:
            time.sleep(1)
            Snake_head.goto(0,0)
            Snake_head.direction = "stop"
            
             #   hide the squares
            for s in square:
                s.goto(1000,1000)
        
            #   Clear the list
            square.clear()

            #   Reset the score
            score = 0

            pen.clear()
            pen.write(f"Score   {score}|   High Score    {high_score}|",align ="center", font = ("courier",24,"normal" ))



    #pythagorem theorem?
    
    time.sleep(d)

w.mainloop()