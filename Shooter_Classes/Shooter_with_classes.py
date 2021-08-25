import turtle
import random
import math


#   Setup screen
w = turtle.Screen()
w.bgcolor("black")
w.bgpic("v.gif")
w.title("Classic Shooter with Classes")

#   Border creation
class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(300,-300)
        self.pendown()
        self.goto(300,300)
        self.goto(-300,300)
        self.goto(-300,-300)
        self.goto(300,-300)
#   Player class is the child of the turtle class, what turtle can do player also can
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("blue")
        self.shape("triangle")
        self.speed = 1
    
    def move(self):
        self.forward(self.speed)

        #   Border Checking
        if self.xcor()>290 or self.xcor()<-290:
            self.left(60)
        if self.ycor()>290 or self.ycor()<-290:
            self.left(60)
        
    def turn_left(self):
        self.left(30)
    def turn_right(self):
        self.right(30)
    def increase_speed(self):
        self.speed += 1
    def reduce_speed(self):
        self.speed -= 1
#   Create Enemy
class Enemy(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("black")
        self.shape("circle")
        self.speed = 3
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random.randint(0,360))

    def respawn(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random.randint(0,360))
    
    def move(self):
        self.forward(self.speed)

        #   Border Checking
        if self.xcor()>290 or self.xcor()<-290:
            self.left(60)
        if self.ycor()>290 or self.ycor()<-290:
            self.left(60)

class Score(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(0,260)
        self.score = 0
    
    def update_score(self):
        self.clear()
        self.write(f"Score   {self.score}|",align ="center", font = ("courier",24,"normal" ))

    def change_score(self,points):
        self.score += points
        self.update_score()



        
def isCollision(t1,t2):
    a = t1.xcor() - t2.xcor()
    b = t1.ycor() - t2.ycor()
    distance = math.sqrt((a**2)+(b**2))

    if distance < 20:
        return True
    else:
        return False
    

     
#   This is called a class instance
#   Use py theorem to check distance because triangle
player = Player()
border = Border()
score = Score()

#   Draw the border
border.draw_border()

#   Create multiple enemies
enemies = []
for i in range(6):
    enemies.append(Enemy())

#   Keyboard binding 
w.listen()
w.onkeypress(player.turn_left,"a")
w.onkeypress(player.turn_right,"d")
w.onkeypress(player.increase_speed,'w')
w.onkeypress(player.reduce_speed,'s')

#   Speeds up the game
w.tracer(0)     #   Stops the screen from being updated

#   Main loop
while True:
    w.update()
    player.move()
    
    for enemy in enemies:
        enemy.move()

        #   check collision between player and enemy
        if isCollision(player,enemy):
            enemy.respawn()
            score.change_score(10)
            


    



