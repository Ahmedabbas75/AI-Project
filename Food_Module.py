import pygame
from pygame.locals import *
import random

class Food:
    def __init__(self,Screen) -> None:
        self.Screen = Screen
        self.Food_pos = [120,120]
        self.Food_image =pygame.transform.smoothscale(pygame.image.load("resources/apple.jpg").convert_alpha(),(40,40)) 

    def Draw_Food(self):
        self.Screen.blit(self.Food_image,(self.Food_pos[0],self.Food_pos[-1]))
        pygame.display.flip() # allow changes to occur

    # move position of food randomly
    def Move_food(self):
        self.Food_pos = [random.randint(1,15) * 40, random.randint(1,15) * 40]



