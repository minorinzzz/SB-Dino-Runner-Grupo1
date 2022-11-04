from pygame.sprite import Sprite
from dino_runner.utils.constants import HEART

class Heart(Sprite):

    def __init__(self,x_pos=100, y_pos=35):
        self.image = HEART[0]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = x_pos
        self.image_rect.y = y_pos
        
    def update(self):
        self.image = HEART[1]

    def draw(self,screen):
        screen.blit(self.image, self.image_rect)