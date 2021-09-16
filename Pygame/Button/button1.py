import pygame, sys

from pygame import mouse


class Button:
    def __init__(self,text,but_width,but_height,pos,elevation):
        #   button core
        self.button_press = False

        self.elevation = elevation
        self.original_pos = pos[1]
        self.change_elevation = elevation

        #   top rectangle
        self.top_rect = pygame.Rect(pos,(but_width,but_height))
        self.top_rect_colour = "light green"

        #   bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(but_width,elevation))
        self.bottom_rect_colour = "dark green"

        #   text
        self.text_surface = basic_font.render(text,True,"black")
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_pos - self.change_elevation

        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.change_elevation 

        #   draw the rects
        pygame.draw.rect(screen,self.bottom_rect_colour,self.bottom_rect,border_radius = 12)
        pygame.draw.rect(screen,self.top_rect_colour,self.top_rect,border_radius = 12)
        screen.blit(self.text_surface,self.text_rect)
        
        self.check_collision()


    def check_collision(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.change_elevation = 0
                self.button_press = True
            else:
                self.change_elevation = self.elevation
                if self.button_press == True:
                    print("clicked!")
                    self.button_press = False
        else:
            self.top_rect_colour = "light green"
            self.change_elevation = self.elevation

pygame.init()
clock = pygame.time.Clock()

width,height = 700,700
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("button experiment")

basic_font = pygame.font.Font(None,50)


button1 = Button("Hi",250,100,(300,200),6)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill("grey")
    button1.draw()

    pygame.display.update()
    clock.tick(60)

