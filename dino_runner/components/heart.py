from pygame.sprite import Sprite
from dino_runner.utils.constants import HEART

class Heart(Sprite):

    def __init__(self,x_pos=100, y_pos=35):
        self.image = HEART[0]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = x_pos
        self.image_rect.y = y_pos
        
    def update(self,speed = 0,my_type=0):
        if my_type == 1:
            self.image = HEART[1]
        elif my_type ==2:
            self.image = HEART[0]
        else:
            self.image_rect.x -= speed

    def draw(self,screen):
        screen.blit(self.image, self.image_rect)