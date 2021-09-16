import pygame,sys

pygame.init()
clock = pygame.time.Clock()

width, height = 800,600
screen = pygame.display.set_mode((width,height))

#   text)
main_font = pygame.font.Font(None,90)
text = "Ha u doin"

# background image
bg_surface = pygame.image.load('space.png')
bg_surface = pygame.transform.scale(bg_surface,(800,600))
bg_rect = bg_surface.get_rect(topleft = (0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(bg_surface,bg_rect)

    text_surface = main_font.render(text,True,"white")
    text_rect = text_surface.get_rect(center = (width/2,height/2))

    screen.blit(text_surface,text_rect)
    

    pygame.display.flip()
    clock.tick(60)