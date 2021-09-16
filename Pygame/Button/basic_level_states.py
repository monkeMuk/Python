import pygame,sys


class GameState:
    def __init__(self):
        self.state = "intro"
        self.level_index = 0

    def state_manager(self):
        if self.state == "intro":
            self.intro()
        if  self.state == "level_1":
            self.level_1()
        if  self.state == "level_2":
            self.level_2()
    
    def intro(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "level_1"

        window.fill("black")

        text_surface = font.render("INTRO",True,"white")
        text_rect = text_surface.get_rect(center = (width/2,height/2))
        window.blit(text_surface,text_rect)
    
    def level_1(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "level_2"

        window.fill("blue")

        text_surface = font.render("LEVEL 1",True,"white")
        text_rect = text_surface.get_rect(center = (width/2,height/2))
        window.blit(text_surface,text_rect)

    def level_2(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "intro"

        window.fill("red")

        text_surface = font.render("LEVEL 2",True,"white")
        text_rect = text_surface.get_rect(center = (width/2,height/2))
        window.blit(text_surface,text_rect)
    
pygame.init()
clock = pygame.time.Clock()

width,height = 500,500
window = pygame.display.set_mode((width,height))

font = pygame.font.Font(None,40)

game_state = GameState()

while True:

    game_state.state_manager()


    pygame.display.update()
    clock.tick(60)
