from dino_runner.components.dinosaur import Dinosaur
import pygame, random
from dino_runner.components.cloud import Cloud
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, GAMEOVER, RESET
from dino_runner.components.obstacles.obstacle_handler import ObstacleHandler
from dino_runner.utils.text_utils import draw_any_message
from dino_runner.components.heart import Heart
from dino_runner.components.powers.hammer import Hammer
from dino_runner.components.powers.shield import Shield


class Game:
    SECONDS_ANIMATION = 10
    MAX_LIVES_GAME = 4
    GAME_SPEED_INITIAL = 20
    GENERAL_X_POS = 130
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.dinosaur = Dinosaur()
        self.max_lives=self.MAX_LIVES_GAME
        self.clouds = [Cloud(),Cloud(),Cloud(),Cloud(),Cloud()]
        self.obstacle_handler = ObstacleHandler()
        self.playing = False # all the game
        self.start = True #screen start
        self.running = True
        self.game_speed = self.GAME_SPEED_INITIAL
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.max_point = 0
        #self.end_game = False
        self.lives = self.MAX_LIVES_GAME
        self.hearts = []
        
    
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
            self.obstacle_handler.update(self)
            self.update_score()
            #actualizacion de nubes
            for i in range(0,len(self.clouds)):
                self.clouds[i].update(self.game_speed + (i*5))
            #actualizacion de nubes
            for i in range(0, len(self.hearts)):
                if i+1>self.lives:
                    self.hearts[i].update(my_type=1)
                else:
                    self.hearts[i].update(my_type=2)
                    
            if self.lives == 0: #aqui me morí totalmente
                if self.points > self.max_point:
                    self.max_point = self.points
                #self.playing = False
                self.reset_attributes()

        else: # por si no estoy en el menu o pantalla de carga
            self.dinosaur.update(dino_event)
            if dino_event[pygame.K_UP] or dino_event[pygame.K_SPACE] or dino_event[pygame.K_KP_ENTER]:# si presiono una de estas comienza el juego
                self.start = False
                self.lives = self.MAX_LIVES_GAME
                for i in range (0,self.max_lives):
                    self.hearts.append(Heart(120+i*30))
 
    def reset_attributes(self):
        self.playing = True
        self.dinosaur = Dinosaur()
        self.obstacle_handler = ObstacleHandler()
        self.start = True
        self.max_lives=self.MAX_LIVES_GAME
        self.points = 0
        self.hearts = []
        self.game_speed=self.GAME_SPEED_INITIAL

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))  #color de fondo
        
        if not self.start:
            self.draw_background()

            # dibujar todas las nubes
            for i in range(0,len(self.clouds)):
                self.clouds[i].draw(self.screen)

            #dibujar las vidas
            for i in range (0,self.max_lives):
                self.hearts[i].draw(self.screen)
            draw_any_message(self.screen, "Lives:",70,50)
            self.draw_powers(self.screen)
            self.dinosaur.draw(self.screen)
            self.obstacle_handler.draw(self.screen)

            message = "Max points: "+str(self.max_point) +"  Points: " + str(self.points)

            if (self.points>= self.max_point and self.points <= self.max_point +self.SECONDS_ANIMATION) or (self.points>= self.max_point+self.SECONDS_ANIMATION*2 and self.points <= self.max_point +self.SECONDS_ANIMATION*3) or (self.points>= self.max_point+self.SECONDS_ANIMATION*4 and self.points <= self.max_point +self.SECONDS_ANIMATION*5)  :
                draw_any_message(self.screen, message, SCREEN_WIDTH - 200, 50, 25,color=(137,14,154))
            else:
                draw_any_message(self.screen, message, SCREEN_WIDTH - 200, 50, 25)

            
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
    
    def draw_powers(self, screen): # dibuja los poderes dependiendo de los que tiene el dinosaurio
        draw_any_message(self.screen, "Power:",75,95)
        for i in range(0, self.dinosaur.dino_hammer):
            Hammer(self.GENERAL_X_POS +i*35, 70).draw(screen)
        if self.dinosaur.dino_shield:
            Shield(self.GENERAL_X_POS, 70).draw(screen)
    
    def draw_screen_start(self): # mi pantalla de inicio y de muerte
        message_any = "Press any key to start"
        #FIN DEL JUEGO, MUERTE
        if self.lives == 0:
            message2="Max points: "+str(self.max_point)
            self.dinosaur.dead()
            self.screen.blit(GAMEOVER, (SCREEN_WIDTH//2-190, SCREEN_HEIGHT//2-25)) #dibujarlo en x y en y
            self.screen.blit(RESET,(SCREEN_WIDTH//2-35, SCREEN_HEIGHT//2+25))
            draw_any_message(self.screen,message2, pos_y = SCREEN_HEIGHT-100)
            draw_any_message(self.screen, message_any, pos_y=SCREEN_HEIGHT-50)
        else: 
             draw_any_message(self.screen, message_any, pos_y=SCREEN_HEIGHT//2)

    def update_score(self): #recargar el score
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed +=1