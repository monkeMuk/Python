import pygame,sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30,40))
        self.image.fill("black")
        self.rect = self.image.get_rect(center = (100,100))
        
        self.gravity = 0
    
    def apply_gravity(self):
        self.gravity += 0.5
        self.rect.y += self.gravity

        if self.rect.bottom >= 500:
            self.rect.bottom = 500
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.bottom == 500:
            self.gravity = -15
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        
    
    def update(self):
        self.apply_gravity()
        self.player_input()
        

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((600,100))
        self.image.fill("brown")
        self.rect = self.image.get_rect(topleft = (0,500))


class Box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill("green")
        self.rect = self.image.get_rect(center = (400,300))
    
    def collision(self):
        if self.rect.colliderect(player.rect):
            self.image.fill("red")
        else:
            self.image.fill("green")

    def update(self):
        self.collision()


#   create ground
#   create 2d player that can jump - simulate gravity

pygame.init()
clock = pygame.time.Clock()

width, height = 600, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("octorun")


player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)

box = Box()
box_group = pygame.sprite.Group()
box_group.add(box)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

    
    screen.fill("light blue")

    player_group.draw(screen)
    player_group.update()

    ground_group.draw(screen)

    box_group.draw(screen)
    box_group.update()

    pygame.display.flip()

    clock.tick(60)
