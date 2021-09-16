import pygame,sys,random

class Main:
    def __init__(self):
        self.state = "intro"
    
    def state_manager(self):
        if self.state == "intro":
            self.intro()
        if self.state == "main_game":
            self.main_game()
    
    def intro(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "main_game"

        screen.fill("grey")
        #   button(self,text,top_colour,bot_colour,pos_x,pos_y,but_height,but_width):
        self.button("Welcome","light blue","dark blue",200,200,100,250)
        #   just_text(self,text,pos_x,pos_y)
        self.just_text("Press SPACEBAR to continue",300,40)

    def main_game(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "intro"
            if event == pygame.KEYDOWN:
                self.user_text += event.unicode

        screen.fill("light blue")

        
        self.just_text("MAIN GAME",280,200)
        
        #    math logic
        
        x = random.randint(0,99)
        y = random.randint(0,99)
        z = x * y

        self.just_text(f"{x} x {y} == ?",300,300)
        #self.just_text("multiplication",250,100)

    def button(self,text,top_colour,bot_colour,pos_x,pos_y,but_height,but_width): 
    

        #   top rect
        self.top_rect = pygame.Rect(pos_x,pos_y,but_width,but_height)
        self.top_rect_colour = top_colour

        #   bot rect
        self.bot_rect = pygame.Rect(pos_x,pos_y + 6, but_width,but_height) # pos[1] always +6
        self.bot_rect_colour = bot_colour

        #   text
        self.text_surface = font.render(text,False,"black")
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)


        

        #   draw the rects
        pygame.draw.rect(screen,self.bot_rect_colour,self.bot_rect,border_radius = 12)
        pygame.draw.rect(screen,self.top_rect_colour,self.top_rect,border_radius = 12)
        screen.blit(self.text_surface,self.text_rect)

    def just_text(self,text,pos_x,pos_y):
        
        #   text
        self.text_surface = font.render(text,False,"black")
        self.text_rect = self.text_surface.get_rect(center =(pos_x,pos_y))
        screen.blit(self.text_surface,self.text_rect)
        
     

pygame.init()
clock = pygame.time.Clock()

width, height = 600,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Multiplication game")

font = pygame.font.Font("font2/Pixeltype.ttf",50)

user_text = ""

main = Main()

while True:
    
    main.state_manager()

    pygame.display.update()
    clock.tick(60)