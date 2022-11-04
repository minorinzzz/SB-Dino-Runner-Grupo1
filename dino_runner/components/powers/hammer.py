from pygame.sprite import Sprite
from dino_runner.utils.constants import HAMMER, SCREEN_WIDTH

class Hammer(Sprite):

    def __init__(self, pos_x = SCREEN_WIDTH, pos_y= 322):
        self.image = HAMMER
        self.image_rect = self.image.get_rect()
        self.image_rect.x = pos_x
        self.image_rect.y = pos_y

    def update(self,speed):
        self.image_rect.x -= speed

    def draw(self,screen):
        screen.blit(self.image, self.image_rect)