import pygame,sys

pygame.init()
clock = pygame.time.Clock()

width, height = 600,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Multiplication game")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("grey")

    box_surf = pygame.Surface((50,50))
    box_surf.fill("green")
    box_rect = box_surf.get_rect(center = (100,100))

    screen.blit(box_surf,box_rect,border_radius = 12)

    pygame.display.update()
    clock.tick(60)