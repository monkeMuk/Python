import pygame, sys

from pygame import draw


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((75,75))
        self.image.fill("red") 
        self.rect = self.image.get_rect(center = (100,300))
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]) 

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.Surface((30,10))
        self.image.fill("black")
        self.rect = self.image.get_rect(center = (pos_x,pos_y))

    def update(self):
        self.rect.x += 5 

        if self.rect.x > width + 200:
            self.kill()
            print("removed")
    


#   setup
pygame.init()
clock = pygame.time.Clock()
#   screen
width, height = 500,500
screen = pygame.display.set_mode((width,height))

#   Player instance
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

pygame.mouse.set_visible(False)

#   Bullet instance
bullet_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())

    screen.fill("white")


    bullet_group.draw(screen)
    bullet_group.update()

    player_group.draw(screen)
    player_group.update()

    pygame.display.flip()
    clock.tick(60)

