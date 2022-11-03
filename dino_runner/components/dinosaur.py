from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEAD
import pygame
from pygame.sprite import Sprite

class Dinosaur(Sprite):

    DINO_X_POS = 50
    DINO_Y_POS = 300
    DINO_Y_POS_DUCK = 340
    INITIAL_STEP = 0
    MAX_STEP = 10
    ACELERATION = 4
    REDUCE_VELOCITY = 0.9
    INITIAL_VELOCITY = 10

    def __init__(self):
        self.image = RUNNING[0]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS
        self.step = self.INITIAL_STEP
        self.dino_jump = False
        self.dino_run = True
        self.dino_duck = False
        self.dino_dead = False
        self.dino_velocity=self.INITIAL_VELOCITY

#eventos por teclado, como se desplazaria si salto
#hacer aparecer una nube en la pantalla cloud.png
#elemento estatico, por ejemplo la vida restante con smallheart

    def update(self, dino_event):
        if self.dino_jump:
            self.jump()
        if self.dino_run and not self.dino_dead:
            self.run()
        if self.dino_duck:
            self.duck()
        
        
        if dino_event[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False

        if dino_event[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False

        elif not self.dino_jump:
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

        if self.step > self.MAX_STEP:
            self.step = self.INITIAL_STEP

        

    def run(self):
        self.image = RUNNING[0] if self.step <= 5 else RUNNING[1]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS
        self.step+=1
        
    def jump(self):
        self.image = JUMPING 
        if self.dino_jump:
            self.image_rect.y -= self.dino_velocity * self.ACELERATION
            self.dino_velocity -= self.REDUCE_VELOCITY
        if self.dino_velocity < -self.INITIAL_VELOCITY:
            self.image_rect.y = self.DINO_Y_POS
            self.dino_jump = False
            self.dino_velocity = self.INITIAL_VELOCITY
            self.dino_run=True

# IMPLEMENTAR AGACHARSE

    def duck(self):
        self.image = DUCKING[0] if self.step <= 5 else DUCKING[1]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS_DUCK
        self.step+=1

    def dead(self):
        self.image = DEAD
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS

        
    def draw(self,screen):
        screen.blit(self.image, (self.image_rect.x, self.image_rect.y))
