# Sprites = 2d piece of art
import pygame,sys,random


class Crosshair(pygame.sprite.Sprite):
    def __init__(self ,picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("gunshot.wav")
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair,target_group,True)

        #   If crosshair collides with target group, target group will be deleted             

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        #   crosshair = position of mouse

class Target(pygame.sprite.Sprite):
    def __init__(self,picture_path,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path) 
        self.rect = self.image.get_rect(center = (pos_x,pos_y))

class GameState():
    def __init__(self):
        self.state = "intro"
   
    def state_manager(self):
        if self.state == "intro":
            self.intro()
        elif self.state == "main_game":
            self.main_game()
    
    def intro(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "main_game"

        screen.blit(background,(0,0))
        screen.blit(ready_text,ready_rect)
        crosshair_group.draw(screen )
        crosshair_group.update()

        pygame.display.flip()        

    def main_game(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()
                

        screen.blit(background,(0,0))

        target_group.draw(screen)
        crosshair_group.draw(screen )
        crosshair_group.update()

        pygame.display.flip()

#   General setup
pygame.init()
clock = pygame.time.Clock()
game_state = GameState()

#   Screen
width,height = 800,700
screen = pygame.display.set_mode((width,height) )
background = pygame.image.load("bg_green.png")
background = pygame.transform.scale(background,(800,700))

ready_text = pygame.image.load("text_ready.png")
ready_rect = ready_text.get_rect(center = (width/2,height/2))



pygame.mouse.set_visible(False)
#   makes the mouse arrow invisible when hovering through the screen



#   Crosshair
crosshair = Crosshair("crosshair_outline_small.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#   Target
target_group = pygame.sprite.Group()
for target in range(10):
    rand_x = random.randrange(0,width)
    rand_y = random.randrange(0,height)
    new_target = Target("target_red2_outline.png",rand_x,rand_y)
    target_group.add(new_target)


while True:

    game_state.state_manager()
     
    clock.tick(60)

