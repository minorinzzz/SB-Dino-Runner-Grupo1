from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD
import pygame
import random
from pygame.sprite import Sprite

class Cloud(Sprite):

    CLOUD_Y_POS = 100
    LESS_SPEED = 10

    def __init__(self,x_pos = SCREEN_WIDTH):
        self.image=CLOUD
        self.image_rect = self.image.get_rect()
        self.image_rect.x = x_pos
        self.image_rect.y = random.randint(50,250)

    def update(self,speed):
        self.image_rect.x -= speed-self.LESS_SPEED

        if self.image_rect.x < -self.image_rect.width:
            self.image_rect.x = SCREEN_WIDTH
            self.image_rect.y = random.randint(50,250)
    
    def draw(self, screen):
        screen.blit(self.image,self.image_rect)
