# Sprites = 2d piece of art
import pygame,sys,random

from pygame.constants import K_RETURN, K_SPACE


class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("Sprites/Sprites_Animation/attack_1.png"))
        self.sprites.append(pygame.image.load("Sprites/Sprites_Animation/attack_2.png"))
        self.sprites.append(pygame.image.load("Sprites/Sprites_Animation/attack_3.png"))
        self.sprites.append(pygame.image.load("Sprites/Sprites_Animation/attack_4.png"))
        self.sprites.append(pygame.image.load("Sprites/Sprites_Animation/attack_5.png"))
        self.sprites.append(pygame.image.load("Sprites/Sprites_Animation/attack_6.png"))
        self.sprites.append(pygame.image.load("Sprites/Sprites_Animation/attack_7.png"))
        self.sprites.append(pygame.image.load("Sprites/Sprites_Animation/attack_8.png"))
        self.sprites.append(pygame.image.load("Sprites/Sprites_Animation/attack_9.png"))
        self.sprites.append(pygame.image.load("Sprites/Sprites_Animation/attack_10.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        #self.image = pygame.transform.scale(self.image(300,300))
        
        self.rect = self.image.get_rect(topleft = (pos_x,pos_y))
    
    def animate(self):
        self.is_animating = True
    
    def deanimate(self):
        self.is_animating = False


    def update(self):
        if self.is_animating == True:

            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites ):
                self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]    
        

         
        

#   General setup
pygame.init()
clock = pygame.time.Clock()

#   Load screen 
width,height = 400,400
screen = pygame.display.set_mode((width,height)) 
pygame.display.set_caption("Sprite Animation")


#   Player instance
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame[K_RETURN]:
                player.animate()
            if event.key == pygame[K_SPACE]:
                player.deanimate()           
    
    #   Drawing
    screen.fill("black")
    moving_sprites.draw(screen)
    moving_sprites.update( )
    pygame.display.flip()
            
     
    pygame.display.flip()
    clock.tick(60)

