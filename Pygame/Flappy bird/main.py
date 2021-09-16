import pygame,sys

pygame.init()
screen_height = 800
screen_width = 600
screen = pygame.display.set_mode((screen_height,screen_width))
clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

        screen.fill("black")
    
    pygame.display.update()
    clock.tick(60)