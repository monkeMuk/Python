import pygame,sys
from pygame import mouse


class Button:
    def __init__(self,text,but_width,but_height,pos,elevation):

        #   button core
        self.pressed = False

        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        #   top rectangle
        self.top_rect = pygame.Rect(pos,(but_width,but_height))
        self.top_color = "light blue"
        #   bottom rectange
        self.bottom_rect = pygame.Rect(pos,(but_width,elevation))
        self.bottom_color = "dark blue"


        #   text
        self.text_surf = gui_font.render(text,True,"black")
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
    
    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation


        self.text_rect.center = self.top_rect.center
        #   this makes the text goes down the same with rest of button

        
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height  = self.top_rect.height + self.dynamic_elevation 

        pygame.draw.rect(screen,self.bottom_color,self.bottom_rect,border_radius = 12)        
        pygame.draw.rect(screen,self.top_color,self.top_rect,border_radius = 12)
        #   border radius makes the borders less sharp
        screen.blit(self.text_surf,self.text_rect)
        
        self.click_check()

    def click_check(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0 
                self.pressed = True 
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    print("CLICK")
                    
                    self.pressed = False
                #   RUNS THE CODE WHEN THE PLAYER RELEASES THE BUTTON
        else:
            self.top_color = "light blue"
            self.dynamic_elevation = self.elevation

            # if mouse_pos != self.top_rect, colour changes 
            # from dark blue back to its default colour
            

        """
        line 24
        if mouse_pos.collidepoint(self.top_rect):
            print("collision!")
        returns this : AttributeError: 'tuple' object has no attribute 'collidepoint'
        
        line 25
        if pygame.mouse.get_pressed():
            this returns (False,False,False) by default
            use [0],[1],[2] to indicate if lmb/mmb/rmb being clicked 
                
        """
        


pygame.init()
clock = pygame.time.Clock()

width,height = 600,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Button Game")

gui_font = pygame.font.Font(None,30)

button1 = Button("Don't Click!",250,50,(width/2,height/2),6)
# 6 is the "bounce"

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    
    screen.fill("grey")
    #button1 = Button("Don't Click!",250,50,(width/2,height/2),6)

    button1.draw()
    
    pygame.display.update()
    clock.tick(60)
        
"""
EXPLANATION 
There are 2 rectangles. the top rect incresed by the value of elevation by default.
When the mouse button is pushed, elevation value is set to 0 so the button is set to its
actual original value which is lower since before this the elevation value was added.
"""
