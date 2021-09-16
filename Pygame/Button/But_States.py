"""
learn how to connect one class to another
"""
import pygame,sys
from pygame import mouse

class Button:
    def __init__(self,text,top_rect_colour,bottom_rect_colour,pos,but_width,but_height,elevation):
        #   button core
        self.press = False

        self.elevation = elevation
        self.delta_elevation = elevation
        self.original_y_pos = pos[1]


        #   sound
        self.click_sound = pygame.mixer.Sound("click.wav")

        #   top rect
        self.top_rect = pygame.Rect(pos,(but_width,but_height))
        self.top_colour = top_rect_colour

        #   bottom rect
        self.bottom_rect = pygame.Rect(pos,(but_width,elevation))
        self.bottom_colour = bottom_rect_colour

        #   text
        self.text_surface = font.render(text,False,"black")
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)

    def click_effect(self):
        self.click_sound.play()

    def draw(self):
        #   elevate logic
        self.top_rect.y = self.original_y_pos - self.delta_elevation

        #   make sure text is pos is the same as the top rect
        self.text_rect.center = self.top_rect.center
        #   make sure the size of the 
        self.bottom_rect.midtop = self.top_rect.midtop 
        self.bottom_rect.height = self.top_rect.height + self.delta_elevation

        #   draw the rects
        pygame.draw.rect(window,self.bottom_colour,self.bottom_rect, border_radius = 12)
        pygame.draw.rect(window,self.top_colour,self.top_rect, border_radius = 12)
        window.blit(self.text_surface,self.text_rect)

        #   activating the mouse_check 
        self.mouse_check()
        
        #   use space bar instead

        
    def mouse_check(self):

        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.delta_elevation = 0
                self.press = True
            else:
                self.delta_elevation = self.elevation
                
                if self.press == True:
                    self.click_effect()
                    print("check!")

                    self.press = False
        else:
            self.top_colour =  self.top_colour
            self.delta_elevation = self.elevation

class GameState():
    def __init__(self):
        self.state = "intro"
    
    
    def state_manager(self):
        if self.state == "intro" :
            self.intro()
        if self.state == "level_1":
            self.level_1()
        if self.state == "level_2":
            self.level_2()

    def intro(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "level_1"
    
        window.fill("black")
        button_intro.draw()

    def level_1(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "level_2"
    
        window.fill("grey")
        button_1.draw()
        pass

    def level_2(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "intro"
    
        window.fill("purple")
        button_2.draw()
        pass
    
    
pygame.init()
clock = pygame.time.Clock()
game_state = GameState()

width,height = 800,600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("another try at making a working button")

font = pygame.font.Font(None,30)



#   button instance
button_intro = Button("intro","pink","red",(300,300),200,150,6)
button_1 = Button("Level 1","light green","dark green",(300,300),200,150,6)
button_2 = Button("Level 1","light blue","dark blue",(300,300),200,150,6)

#   text,top_rect_colour,bottom_rect_colour,pos,but_width,but_height,elevation

while True:

    game_state.state_manager()
    pygame.display.update()

    clock.tick(60)