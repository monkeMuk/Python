import pygame
from support import import_folder 

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,surface):     #   not sure why we need surface
        super().__init__()
        
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15 

        #self.image = pygame.Surface((50,30))
        #self.image.fill('red')
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        #   Player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
        self.gravity = 0.5
        self.jump_speed = -12

        #   Player status:
        self.status = "idle"
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False 
    
    def import_character_assets(self):
        character_path = 'graphics/character/'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
            #   needs some more revision 


    def animate(self):
        animation = self.animations[self.status]

        #   loop over index frame
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)] # local variable 
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image 
            """
            (surface,[0],[1])
            if [0] is True:
                surface is flipped horizontally ( x axis)
            if [1] is True:
                surface is flipped vertically( y axis)
            """
                # set the rect
        #   on_ground
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright) # player on the ground and hits the right wall
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)

        #   on_ceiling
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright) # player on the ground and hits the right wall
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)

    def get_status(self):
        if self.direction.y > 0.8:  # or any number higher than the self.gravity value
            self.status = 'fall'
        #  y > 0 = fall because as you go downwards y value increases
        elif self.direction.y < 0: 
            self.status = 'jump'
        else:
            #if self.direction.x > 0 or self.direction.x < 0:  longer way to write it
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'
        
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1 
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            #self.direction.y = self.jump_speed
            self.jump()

    def jump(self):
        self.direction.y = self.jump_speed

    def apply_gravity(self): 
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
