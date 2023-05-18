import pygame
import random

from Snake_Module import Snake
class Food:
    def __init__(self, Screen) -> None:
        self.Screen = Screen
        self.Food_pos = [120, 120]
        self.Food_image = pygame.image.load("resources/food.jpg").convert()
    def Draw_Food(self):
        self.Screen.blit(self.Food_image, (self.Food_pos[0], self.Food_pos[-1]))

    # move position of food randomly
    def Move_food(self):
        self.Food_pos = [random.randint(1, 13) * 40, random.randint(1, 13) * 40]
        