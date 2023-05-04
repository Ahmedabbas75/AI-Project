# import module we need in project
import pygame
from Snake_Module import *
from Food_Module import *

class GameWindow:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("AI Project")
        self.snake = Snake(self.window, 2)
        self.snake.Draw_Snake()
        self.food = Food(self.window)
        self.food.Draw_Food()
        self.clock = pygame.time.Clock()
        self.old_tick = 0

    def time_update(self):
        ticks = pygame.time.get_ticks()
        if ticks - self.old_tick > 200:
            self.snake.Snake_Walk()
            self.old_tick = ticks

    # check if snake ate the food
    def Check_ate_Food(self):
        return [self.snake.Snake_pos_X[0], self.snake.Snake_pos_Y[0]] == self.food.Food_pos
         

    def Play_Game(self):
        pygame.display.update()
        self.window.fill((110, 110, 5))
        self.clock.tick(60)
        self.time_update()

        if self.Check_ate_Food():
            self.snake.increase_Snake_lenght()
            self.food.Move_food()

        self.food.Draw_Food()
        self.snake.Draw_Snake()

    # running window win running variable equle to True
    def Run(self, Running=True):
        while Running:
            self.Play_Game()
            
            # allaw window to receive input from keyboard
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Running = False

                    if event.key == pygame.K_LEFT:
                        self.snake.change_direction("left")

                    if event.key == pygame.K_RIGHT:
                        self.snake.change_direction("right")

                    if event.key == pygame.K_UP:
                        self.snake.change_direction("up")

                    if event.key == pygame.K_DOWN:
                        self.snake.change_direction("down")

                # when user want to exit window game
                elif event.type == pygame.QUIT:
                    Running = False



if __name__ == '__main__':
    Game = GameWindow()
    Game.Run()
