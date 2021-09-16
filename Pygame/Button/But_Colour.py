import pygame,sys



class Button:
    def __init__(self,text,top_rect_colour,bottom_rect_colour,pos,but_width,but_height,elevation):
        #   button core
        self.press = False

        self.elevation = elevation
        self.delta_elevation = elevation
        self.original_y_pos = pos[1]

        #   top rect
        self.top_rect = pygame.Rect(pos,(but_width,but_height))
        self.top_colour = top_rect_colour

        #   bottom rect
        self.bottom_rect = pygame.Rect(pos,(but_width,elevation))
        self.bottom_colour = bottom_rect_colour

        #   text
        self.text_surface = font.render(text,False,"black")
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)

    
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
        
    def mouse_check(self): 
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.delta_elevation = 0
                self.press = True
            else:
                self.delta_elevation = self.elevation
                if self.press == True:
                    print("check!")
                    self.press = False
        else:
            self.top_colour =  self.top_colour
            self.delta_elevation = self.elevation
                
            
        


pygame.init()
clock = pygame.time.Clock()

width,height = 800,600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("another try at making a working button")

font = pygame.font.Font(None,30)

#   button instance
button1 = Button("Hello!","pink","red",(300,300),200,150,6)
#   text,top_rect_colour,bottom_rect_colour,pos,but_width,but_height,elevation

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    window.fill("black")
    button1.draw()

    pygame.display.update()

    clock.tick(60)