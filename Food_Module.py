import pygame
import random
class Food:
    def __init__(self, Screen) -> None:
        self.Screen = Screen
        self.Food_pos = [120, 120]
        self.Food_image = pygame.transform.smoothscale(pygame.image.load("resources/food.jpg").convert_alpha(), (40, 40))

    def Draw_Food(self):
        self.Screen.blit(self.Food_image, (self.Food_pos[0], self.Food_pos[-1]))

    # move position of food randomly
    def Move_food(self):
        # while self.Food_pos is None:
        #     new_food_pos = [random.randint(1, 15) * 40, random.randint(1, 15) * 40]
        #     for i in range(Snake.get_Snake_length-1):
        #         self.Food_pos = new_food_pos if new_food_pos != [Snake.get_snake_pos[0][i], Snake.get_snake_pos[1][i]] else None
        self.Food_pos = [random.randint(1, 13) * 40, random.randint(1, 13) * 40]
