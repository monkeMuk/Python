"""
Rect1.colliderect(Rec2)
returns True if hit
returns False if didn't hit

doesn't tell you where the rects are colliding 
Rect1. collidepoint(x,y)?

"""
import pygame,sys

def bouncing_rect():
    global x_speed,y_speed,other_speed

    moving_rect.x += x_speed
    moving_rect.y += y_speed

    
    #   moving_rext border collision
    moving_rect.x += x_speed
    moving_rect.y += y_speed

    if moving_rect.right  >= width or moving_rect.left <= 0:
        x_speed *= -1
    if moving_rect.bottom >= height or moving_rect.top <=  0:
        y_speed *= -1

    #  other_rect border collision
    other_rect.y += other_speed

    if other_rect.bottom >= height or other_rect.top <= 0:
        other_speed *= -1            
    
    #   Rect collide
    if moving_rect.colliderect(other_rect):

        collision_tolerance = 10

        if abs(other_rect.top - moving_rect.bottom) < collision_tolerance and y_speed:# > 0:
            y_speed *= -1
        if abs(other_rect.bottom - moving_rect.top) < collision_tolerance and y_speed:#< 0:
            y_speed *= -1
        if abs(other_rect.right - moving_rect.left) < collision_tolerance and x_speed:# > 0:
            x_speed *= -1
        if abs(other_rect.left - moving_rect.right) < collision_tolerance and x_speed:# < 0:
            x_speed *= -1

        


    pygame.draw.rect(screen,"blue",moving_rect)
    pygame.draw.rect(screen,"green",other_rect)

pygame.init()
clock = pygame.time.Clock()

width,height = 600,600
screen = pygame.display.set_mode((width,height))

moving_rect = pygame.Rect(200,200,100,100)
x_speed, y_speed = 2,3

other_rect = pygame.Rect(400,100,50,50)
other_speed = 2


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    
    screen.fill("black")


    bouncing_rect()

    pygame.display.flip()
    clock.tick(60)