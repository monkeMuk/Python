#2: 49 54
import pygame
from sys import exit
from random import randint, choice 

class Player(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("graphics/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("graphics/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("graphics/jump.png").convert_alpha()

        self.image = self.player_walk[self.player_index] 
        self.rect = self.image.get_rect(midbottom = (50,300 ))
        self.gravity = 0
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

     
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    
    
    def __init__(self,type):
        super().__init__()
        
        if type == "fly":
            fly_1 = pygame.image.load("graphics/Fly1.png").convert_alpha()
            fly_2 = pygame.image.load("graphics/Fly2.png").convert_alpha()
            self.frames = [fly_1,fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load("graphics/snail1.png").convert_alpha()
            snail_2 = pygame.image.load("graphics/snail2.png").convert_alpha()
            self.frames   = [snail_1,snail_2]
            y_pos = 300
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(700,1100),y_pos))
    
    def animation_state(self):

        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100: self.kill( )

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surface = score_font.render(f"Score: {int(current_time/1000)}",False,(64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)
    return current_time
  
def collisions_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,True):
        return False
    else:
        return True


pygame.init()
WIDTH, HEIGHT = 800,500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Alien Jump")
clock = pygame.time.Clock()
score_font = pygame.font.Font("font/Pixeltype.ttf",50)
game_active = False
start_time = 0
score = 0

#   single and single groups
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

#   Intro screen
player_stand_surf = pygame.image.load("graphics/player_stand.png").convert_alpha()
player_stand_rect = player_stand_surf.get_rect(center = (WIDTH/2,HEIGHT/2))

intro_text_surf = score_font.render("Alien Jump",False,"black")
intro_text_rect = intro_text_surf.get_rect(center =(WIDTH/2,HEIGHT/2-100) ) 
tuto_text_surf = score_font.render("Press SPACE to jump!",False,"black")
tuto_text_rect = tuto_text_surf.get_rect(center =(WIDTH/2,HEIGHT/2+120) ) 

#   Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1400)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(["fly","snail","snail","snail"])))
                
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
                     
    if game_active:
        
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        score = display_score()

        player.draw(screen)
        player.update()

        game_active = collisions_sprite()

        obstacle_group.draw(screen)
        obstacle_group.update()

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand_surf,player_stand_rect)
        screen.blit(intro_text_surf,intro_text_rect)
       
        score_message = score_font.render(f"Your score is {int(score/1000)}",'False',"black")
        score_rect = score_message.get_rect(center = (WIDTH/2, HEIGHT/2 + 120))

        if score == 0:
            screen.blit(tuto_text_surf,tuto_text_rect)
        else:
            screen.blit(score_message,score_rect)

    pygame.display.update()
    clock.tick(60)

