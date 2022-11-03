from dino_runner.components.dinosaur import Dinosaur
import pygame, random
from dino_runner.components.cloud import Cloud
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.obstacles.obstacle_handler import ObstacleHandler
from dino_runner.utils.text_utils import get_text_element


class Game:
    SECONDS_ANIMATION = 10
    MAX_LIVES = 3
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.dinosaur = Dinosaur()
        self.clouds = [Cloud(),Cloud(),Cloud(),Cloud(),Cloud()]
        self.obstacle_handler = ObstacleHandler()
        self.playing = False # all the game
        self.start = True #screen start
        self.running = True
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.max_point = 0
        #self.end_game = False
        self.lives = self.MAX_LIVES

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def reset_attributes(self):
        self.playing = True
        self.dinosaur = Dinosaur()
        self.obstacle_handler = ObstacleHandler()
        self.start = True
        self.points = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Reconoce la X de la ventana
                self.playing = False
       

    def update(self):
        dino_event = pygame.key.get_pressed()
        if not self.start:
            self.dinosaur.update(dino_event)
            self.obstacle_handler.update(self)
            self.update_score()
            #actualizacion de nubes
            for i in range(0,len(self.clouds)):
                self.clouds[i].update(self.game_speed + (i*5))

            if self.lives == 0:
                if self.points > self.max_point:
                    self.max_point = self.points
                #self.playing = False
                self.reset_attributes()

        else: # si presiono una de estas comienza el juego
            self.dinosaur.update(dino_event)
            if dino_event[pygame.K_UP] or dino_event[pygame.K_SPACE] or dino_event[pygame.K_KP_ENTER]:
                self.start = False
                self.lives = self.MAX_LIVES
 

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))  #color de fondo
        
        if not self.start:
            self.draw_background()
            # dibujar todas las nubes
            for i in range(0,len(self.clouds)):
                self.clouds[i].draw(self.screen)

            self.dinosaur.draw(self.screen)
            self.obstacle_handler.draw(self.screen)
            self.draw_score()

        else:
            self.draw_screen_start()
            self.dinosaur.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg)) #dibujarlo en x y en y
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg)) #vuelve a dibujar
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg)) #vuelve a dibujar con cambios en la posicion
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def draw_screen_start(self):
        if self.lives == 0:
            message= "GAME OVER!!"
            self.dinosaur.dead()
        else:
            message = "Press any key to start"
        #message = "Pulse la barra espaciadora o UP para jugar"
        start_text, start_rect = get_text_element(message)
        self.screen.blit(start_text,start_rect)

    def draw_score(self):

        message = "Max points: "+str(self.max_point) +"  Points: " + str(self.points)
        if (self.points>= self.max_point and self.points <= self.max_point +self.SECONDS_ANIMATION) or (self.points>= self.max_point+self.SECONDS_ANIMATION*2 and self.points <= self.max_point +self.SECONDS_ANIMATION*3) or (self.points>= self.max_point+self.SECONDS_ANIMATION*4 and self.points <= self.max_point +self.SECONDS_ANIMATION*5)  :
            points_text, points_rect = get_text_element(message, SCREEN_WIDTH - 200, 50, 25,(137,14,154))
        else:
            points_text, points_rect = get_text_element(message, SCREEN_WIDTH - 200, 50, 25)
        
        self.screen.blit(points_text, points_rect)
    
    def update_score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed +=1

    def show_menu(self):
        self.running = True

        black_color = (0,0,0)
        self.screen.fill(black_color)
        self.show_menu_options()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False 
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                self.run()

    def show_menu_options(self):
        white_color = (255,255,255)
        if self.points > 0:
            text, text_rect = get_text_element("GAME OVER!! ", font_size = 40,color=white_color)
        else:
            text, text_rect = get_text_element("Press any key to start", font_size = 40,color=white_color)
       
        self.screen.blit(text,text_rect)