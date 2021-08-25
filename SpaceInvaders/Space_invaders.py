import turtle
import os
import random

#set up the screen
w = turtle.Screen()
w.bgcolor("black")
w.title("Space Invaders")
w.bgpic("spbg.gif")

#   Register the shapes
#turtle.register_shape("")
#turtle.register_shape("")

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
    border_pen.lt(90)
border_pen.hideturtle()

#   Set the score to 0
score = 0
high_score = 0

#   Draw the score
scorepen = turtle.Turtle()
scorepen.speed(0)
scorepen.color("white")
scorepen.penup()
scorepen.goto(0,260)
scorepen.write("Score    |   High Score    |",align ="center", font = ("courier",24,"normal" ))





#   Player model
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

numofen = 5
enemies = []

for i in range(numofen):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    #   Enemy models
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100,250)
    enemy.setposition(x,y)

enemyspeed = 3

#   Bullets
bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.color("white")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bullet_speed = 20


#   Define bullet states
#   ready - ready to fire
#   fire - bullet is firing - cannot fire 
bulletstate = "ready"



#   moving defs
def move_left():
    x = player.xcor()
    if x < -275:
        player.setx(x)
    else:
        player.setx(x-20)

def move_right():
    x = player.xcor()
    if x > 275:
        player.setx(x)
    else:
        player.setx(x+20)

def fire_bullet():
    #   Declare bulletstate as global if it needs to be chanegd / need more infos
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        """ 
        The difference between = and ==
        = is used to assign value(right) to a variable(left)
        == is an operator and checks if it's true or false
        """
        os.system("afplay se.wav&")
        #   make the bullet appear 10 pixels above the player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x,y + 10) 
        bullet.showturtle()

def isCollision(t1, t2):
    if t1.distance(t2) < 20:
        return True
    else:
        return False


#   Keyboard binding
w.listen()
w.onkeypress(move_left, "a")
w.onkeypress(move_right, "d")
w.onkeypress(fire_bullet,"space")

#   Main game loop
while True:

    for enemy in enemies:
        #   Move the enemy
        x = enemy.xcor()
        enemy.setx(x + enemyspeed)
        #   Move enemy back and forth

        if enemy.xcor() > 280 or enemy.xcor() < -280:
            #   Moves all the enemy down
            for e in enemies:
                y = e.ycor()
                e.sety(y-30)
            #   Change enemy direction
            enemyspeed *= -1
            
        if isCollision(bullet,enemy):
            #   Reset teh bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #   Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100,250)
            enemy.setposition(x,y)
            os.system("afplay be.wav&")


            score += 1
            if score > high_score:
                high_score = score
            scorepen.clear()
            scorepen.write(f"Score   {score}|   High Score    {high_score}|",align ="center", font = ("courier",24,"normal" ))

        
        

        if isCollision(player, enemy):
            #   Reset the player
            player.hideturtle()
            #   Reset the enemy
            enemy.hideturtle()
            print("game over!")
            break 
    
    #   Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        # the bulletspeed determines how fast bullet goes up
        bullet.sety(y + bullet_speed)

    #   check bullet cross top border
    if bullet.ycor()>280:
        bullet.hideturtle()
        bulletstate = "ready"
    #   Check bullet hit enemy
    
