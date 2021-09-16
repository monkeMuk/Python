#2: 49 54
import pygame
from sys import exit
from random import randint 

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surface = score_font.render(f"Score: {int(current_time/1000)}",False,(64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)
    return current_time
    

def obstacle_movement(obstacle_list):
    if obstacle_list:
        # if python finds an empty list, it returns a negative
        for obstacle_rect in obstacle_list:
            obstacle_rect.x  -= 5
            
            if obstacle_rect.bottom == 300: 
                screen.blit(snail_surf,obstacle_rect) 
            elif obstacle_rect.bottom == 210:
                screen.blit(fly_surf,obstacle_rect) 


        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []
    

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): 
                return False
    return True

def player_animation():
    # display walking animation when player on floor
    # display jump surfaces when player's x higher than 300
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]


pygame.init()
WIDTH, HEIGHT = 800,500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Alien Jump")
clock = pygame.time.Clock()
score_font = pygame.font.Font("font/Pixeltype.ttf",50)
game_active = False
start_time = 0

score = 0

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

#   Snails
snail_frame_1 = pygame.image.load("graphics/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("graphics/snail2.png").convert_alpha()
snail_frame_index = 0
snail_frame = [snail_frame_1,snail_frame_2]


#   Flies
fly_frame_1 = pygame.image.load("graphics/Fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("graphics/Fly2.png").convert_alpha()
fly_frame_index = 0
fly_frame = [fly_frame_1,fly_frame_2]


obstacle_rect_list = []

player_walk_1 = pygame.image.load("graphics/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load("graphics/jump.png").convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (50,300))
player_gravity = 0

player_stand_surf = pygame.image.load("graphics/player_stand.png").convert_alpha()
player_stand_rect = player_stand_surf.get_rect(center = (WIDTH/2,HEIGHT/2))

#   Intro screen
intro_text_surf = score_font.render("Alien Jump",False,"black")
intro_text_rect = intro_text_surf.get_rect(center =(WIDTH/2,HEIGHT/2-100) ) 

#   tutotial text
tuto_text_surf = score_font.render("Press SPACE to jump!",False,"black")
tuto_text_rect = tuto_text_surf.get_rect(center =(WIDTH/2,HEIGHT/2+120) ) 

#   Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1400)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,300)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

        if game_active:
                #   Checks if the player is on the floor
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
                #   press space for player to jump
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
            
                #   picks between frame 0 and frame 1 in the index list for animating snail and fly
            #   snail animation with timer
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surf = snail_frame[snail_frame_index]
            
            #   fly animation with timer
            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surf = fly_frame[fly_frame_index]

            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surf.get_rect(midbottom = (randint(700,1100),300)) )
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(midbottom = (randint(700,1100),210)) )

        else:

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
            


           
    if game_active:
        
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        #pygame.draw.rect(screen,"#c0e8ec",score_rect)
        #pygame.draw.rect(screen,"#c0e8ec",score_rect,10)

        #screen.blit(score_surface, score_rect)
        score = display_score()

        #snail_rect.x -= 2
        #if snail_rect.x <= -WIDTH:
            #snail_rect.x = 900
        #screen.blit(snail_surf,snail_rect)

        #   Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300: player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf,player_rect)

        #   Obstacle movement
        obsticle_rect_list =  obstacle_movement(obstacle_rect_list)
        
        #   Collision
        game_active = collisions(player_rect,obstacle_rect_list )

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand_surf,player_stand_rect)
        screen.blit(intro_text_surf,intro_text_rect)

        obstacle_rect_list.clear()
        player_rect.midbottom = (50,300)
        player_gravity = 0
        
        score_message = score_font.render(f"Your score is {int(score/1000)}",'False',"black")
        score_rect = score_message.get_rect(center = (WIDTH/2, HEIGHT/2 + 120))



        if score == 0:
            screen.blit(tuto_text_surf,tuto_text_rect)
        else:
            screen.blit(score_message,score_rect)

    pygame.display.update()
    clock.tick(60)

