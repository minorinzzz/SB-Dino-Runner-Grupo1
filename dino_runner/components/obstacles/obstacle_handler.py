from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SCREEN_WIDTH
import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.powers.shield import Shield
from dino_runner.components.powers.hammer import  Hammer
from dino_runner.components.heart import Heart

class ObstacleHandler():
    def __init__(self):
        self.obstacles = []
        self.now_power = False
        self.ultim_power = "S" #S, H
        self.is_live = False

    def update(self, game):
        if len(self.obstacles) == 0:
            self.now_power = False
            self.is_live = False
            if random.randint(1,2) == 1: #50%
                if random.randint(1,2) == 1: #25%
                    self.obstacles.append(Cactus(LARGE_CACTUS))
                    self.obstacles[0].image_rect.y-=30
                else:#25%
                    if game.dinosaur.dino_shield or game.dinosaur.dino_hammer or random.randint(1,3) <3: #16.6
                        if random.randint(1,3) <3: #11.06%
                            self.obstacles.append(Cactus(SMALL_CACTUS))  
                        else: # 5.53%
                            self.obstacles.append(Heart(SCREEN_WIDTH,250))
                            self.is_live = True
                    else: # 8.3%
                        if random.randint(1,3) <3: #5.53
                            self.obstacles.append(Shield())
                            self.ultim_power="S"
                        else: #2.76%
                            self.obstacles.append(Hammer())
                            self.ultim_power="H"
                        self.now_power = True
            else: # 50%
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed) 

            if game.dinosaur.image_rect.colliderect(obstacle.image_rect): #Colisionan los rectangulos
                if not self.is_live:
                    if not self.now_power:
                        if not game.dinosaur.dino_shield and game.dinosaur.dino_hammer==0:
                            pygame.time.delay(1000)
                            game.lives -= 1
                            if game.max_lives>game.MAX_LIVES_GAME:
                                # en vez de solo desaparecer lo borra de la lista a las vidas super extra (aquellas que se hayan ganado mas que lo maximo de vidas permitidos en el juego)
                                game.max_lives-=1
                                game.hearts.pop()
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
                else:
                    game.lives+=1
                    if game.lives>game.max_lives:
                        game.hearts.append(Heart(120+game.max_lives*30))
                        game.max_lives = game.lives

                self.obstacles.pop() 

            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()
               

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)