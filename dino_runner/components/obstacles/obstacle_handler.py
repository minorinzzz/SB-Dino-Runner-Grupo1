from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleHandler():
    def __init__(self):
        self.obstacles = []
        self.collition = False

    def update(self, speed,dino):
        self.collition=False
        if len(self.obstacles) == 0:
            if random.randint(1,2) == 1:
                if random.randint(1,2) == 1:
                    self.obstacles.append(Cactus(LARGE_CACTUS))
                else:
                    self.obstacles.append(Cactus(SMALL_CACTUS))  
            else:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(speed) 

            if dino.image_rect.colliderect(obstacle.image_rect): #Colisionan los rectangulos
                #print("dino ", dino.image_rect)
                #print("obs ",obstacle.image_rect)
                #dino.dino_dead = True
                #dino.dead()
                #dino.draw(screen)  
                #dino.dino_dead = False
                pygame.time.delay(1000)
                self.obstacles.pop() 
                self.collition = True
                

            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()
                # devuelve true cuando chocaron
        return self.collition #devuelve false si no chocaron en ningun punto

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)