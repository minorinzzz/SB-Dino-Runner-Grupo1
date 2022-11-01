from dino_runner.utils.constants import SMALL_CACTUS
import pygame
from dino_runner.components.obstacles.cactus import Cactus

class ObstacleHandler():
    def __init__(self):
        self.obstacles = []

    def update(self, speed,dino):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(speed)
            if dino.image_rect.colliderect(obstacle.image_rect): #Colisionan los rectangulos
                pygame.time.delay(300)
                self.obstacles.pop() 

            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)