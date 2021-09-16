import turtle
import math

screen_width = 800
screen_height = 600

w = turtle.Screen()
w.setup(screen_width,screen_height)
w.title("Space Arena")
w.bgcolor("black")
w.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("White")
pen.penup()
pen.hideturtle()

class Sprite():
    def __init__(self,x,y,shape,color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0
        self.heading = 0
        self.da = 0
        self.thrust = 0  #  Amount of force being let out by the engine at a certain time
        self.accelaration = 0.2 #   Change in the force ( Speed/ velocity) 

    def update(self):
        self.heading += self.da
        self.heading %= 360

        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust

        self.x += self.dx
        self.y += self.dy

    def render(self,pen):
        pen.goto(self.x, self.y)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()
    
class Player(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, 0, 0, shape, color)
        self.lives = 3
        self.score = 0
        self.heading = 90
        self.da = 0
        
    def rotate_left(self):
        self.da = 5
        
    def rotate_right(self):
        self.da = -5
        
    def stop_rotation(self):
        self.da = 0.0
    
    def accelarate(self):
        self.thrust += self.accelaration
    
    def decelarate(self):
        self.thrust = 0

    
    def render(self,pen):
        pen.shapesize(0.5,1,None) # Turtle object default size is 20 x 20
        pen.goto(self.x, self.y)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()

        pen.shapesize(1.0,1.0, None)
    
#   Create and Instances

player = Player(0,0,"triangle","green")

enemy = Sprite(0,100,"circle","red")
enemy.dx =  -1
enemy.dy = -0.3

powerup = Sprite(0,-100,"circle","blue")
powerup.dx= 1
powerup.dy= 0.1

#   Sprites list
sprites = []
sprites.append(player)
sprites.append(enemy)
sprites.append(powerup)

# Keyboard bindings
w.listen()
w.onkeypress(player.rotate_left, "Left")
w.onkeypress(player.rotate_right, "Right")
w.onkeypress(player.accelarate, "Up")
w.onkeypress(player.decelarate, "Down")

w.onkeyrelease(player.stop_rotation, "Left")
w.onkeyrelease(player.stop_rotation, "Right")
w.onkeyrelease(player.accelarate, "Up")
w.onkeyrelease(player.decelarate, "Down")


while True:
    #   Clears the screen
    pen.clear()
    #   Do game stuff

    for s in sprites:
        #   Updates the sprites
        s.update()
    for s in sprites:
        #   Render thesprites
        s.render(pen)
        



    #   updates the screen
    w.update()