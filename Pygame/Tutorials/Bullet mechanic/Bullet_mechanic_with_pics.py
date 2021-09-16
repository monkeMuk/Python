import pygame,sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect(center = (100,300))
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
    
    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        #   BULLET CLASS 

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.Surface((10,50))
        self.image.fill("red")
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
    
    def update(self):
        self.rect.y -= 6

        if self.rect.y <= 0 - 200:
            self.kill







pygame.init()
clock = pygame.time.Clock()

width, height = 600,600
screen = pygame.display.set_mode((width,height))
pygame.mouse.set_visible(False)

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

bullet_group = pygame.sprite.Group()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())


    
    screen.fill("black")

    bullet_group.draw(screen)
    bullet_group.update()

    player_group.draw(screen)
    player_group.update()


    
    pygame.display.flip()
    clock.tick(60)