from dino_runner.components.dinosaur import Dinosaur
import pygame, random
from dino_runner.components.cloud import Cloud
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.obstacles.obstacle_handler import ObstacleHandler
from dino_runner.utils.text_utils import get_text_element


class Game:
    SECONDS_ANIMATION = 10
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
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.max_point = 0
        self.end_game = False

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Reconoce la X de la ventana
                self.playing = False
       

    def update(self):
        dino_event = pygame.key.get_pressed()
        if not self.start:
            self.dinosaur.update(dino_event)
            self.end_game = self.obstacle_handler.update(self.game_speed,self.dinosaur)
            #actualizacion de nubes
            for i in range(0,len(self.clouds)):
                self.clouds[i].update(self.game_speed + (i*5))

            if self.end_game:
                if self.points > self.max_point:
                    self.max_point = self.points
                self.points = 0

        else: # si presiono una de estas comienza el juego
            self.dinosaur.update(dino_event)
            if dino_event[pygame.K_UP] or dino_event[pygame.K_SPACE] or dino_event[pygame.K_KP_ENTER]:
                self.start = False
 

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
        message = "Pulse la barra espaciadora para jugar"
        start_text, start_rect = get_text_element(message)
        self.screen.blit(start_text,start_rect)

    def draw_score(self):
        self.points += 1
        message = "Max points: "+str(self.max_point) +"  Points: " + str(self.points)
        if (self.points>= self.max_point and self.points <= self.max_point +self.SECONDS_ANIMATION) or (self.points>= self.max_point+self.SECONDS_ANIMATION*2 and self.points <= self.max_point +self.SECONDS_ANIMATION*3) or (self.points>= self.max_point+self.SECONDS_ANIMATION*4 and self.points <= self.max_point +self.SECONDS_ANIMATION*5)  :
            points_text, points_rect = get_text_element(message, SCREEN_WIDTH - 200, 50, 25,(137,14,154))
        else:
            points_text, points_rect = get_text_element(message, SCREEN_WIDTH - 200, 50, 25)
        
        self.screen.blit(points_text, points_rect)