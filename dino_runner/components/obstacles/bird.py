from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
class Bird(Obstacle):

    BIRD_Y_POS = 250

    def __init__(self, images):
        super().__init__(images, 0)
        self.image_rect.y = self.BIRD_Y_POS
        self.step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.image_rect.x,self.image_rect.y)) 
        if self.step == 10:
            self.step = 0
            self.image=BIRD[0]
            self.image_rect.y =self.BIRD_Y_POS

        if self.step == 5:
            self.image=BIRD[1]
            self.image_rect.y = self.BIRD_Y_POS - 13
        self.step+=1
#IMPLEMENTAR PARTE BIRD, en vez de cactus haya ave
