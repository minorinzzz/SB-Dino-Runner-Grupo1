from pygame.sprite import Sprite
from dino_runner.utils.constants import SHIELD, SCREEN_WIDTH

class Shield(Sprite):

    def __init__(self):
        self.image = SHIELD
        self.image_rect = self.image.get_rect()
        self.image_rect.x = SCREEN_WIDTH
        self.image_rect.y = 322

    def update(self,speed):
        self.image_rect.x -= speed

    def draw(self,screen):
        screen.blit(self.image, self.image_rect)