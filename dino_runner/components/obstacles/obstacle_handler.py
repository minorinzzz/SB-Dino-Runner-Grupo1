from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.powers.shield import Shield
from dino_runner.components.powers.hammer import  Hammer

class ObstacleHandler():
    def __init__(self):
        self.obstacles = []
        self.now_power = False
        self.ultim_power = "S" #S, H

    def update(self, game):
        if len(self.obstacles) == 0:
            self.now_power = False
            if random.randint(1,2) == 1:
                if random.randint(1,2) == 1:
                    self.obstacles.append(Cactus(LARGE_CACTUS))
                    self.obstacles[0].image_rect.y-=30
                else:
                    if game.dinosaur.dino_shield or game.dinosaur.dino_hammer or random.randint(1,2) ==1:
                        self.obstacles.append(Cactus(SMALL_CACTUS))  
                    else:
                        if random.randint(1,3) <3:
                            self.obstacles.append(Shield())
                            self.ultim_power="S"
                        else:
                            self.obstacles.append(Hammer())
                            self.ultim_power="H"
                        self.now_power = True
            else:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed) 

            if game.dinosaur.image_rect.colliderect(obstacle.image_rect): #Colisionan los rectangulos
                if not self.now_power:
                    if not game.dinosaur.dino_shield and game.dinosaur.dino_hammer==0:
                        pygame.time.delay(1000)
                        game.lives -= 1
                    else:
                        if game.dinosaur.dino_shield:
                            game.dinosaur.dino_shield = False
                        else:
                            game.dinosaur.dino_hammer -=1
                else:
                    if self.ultim_power == "S":
                        game.dinosaur.dino_shield = True
                    else:
                        game.dinosaur.dino_hammer = random.randint(1,5)
                self.obstacles.pop() 

            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()
               

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)