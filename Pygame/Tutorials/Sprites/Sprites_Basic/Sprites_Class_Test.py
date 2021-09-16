import pygame, sys

width,height = 800,700

pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

current_time = 0
button_press_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            button_press_time = pygame.time.get_ticks()
            screen.fill("white ")
            # records the exact time I pressed the button 
    
    current_time = pygame.time.get_ticks()

    if current_time - button_press_time > 2000:
        screen.fill("black")

        
    print(f"button press time: {button_press_time}")

    pygame.display.flip()
    clock.tick(60)

