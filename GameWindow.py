# import module we need in project
from pygame.locals import *
from Snake_Module import *
from Food_Module import *
import time


class Game_Window:
    def __init__(self):
        pygame.init()
        self.Window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("AI Project")
        self.snake = Snake(self.Window, 2)
        self.snake.Draw_Snake()
        self.food = Food(self.Window)
        self.food.Draw_Food()
        self.clock = pygame.time.Clock()

    # check if snake ate the food
    def Check_ate_Food(self):
        if [self.snake.Snake_pos_X[0], self.snake.Snake_pos_Y[0]] == self.food.Food_pos:
            return True
        return False

    def Play_Game(self):
        self.Window.fill((110, 110, 5))
        self.clock.tick(60)
        self.snake.Snake_Walk()
        if self.Check_ate_Food():
            self.snake.increase_Snake_lenght()
            self.food.Move_food()

        self.food.Draw_Food()

    # running window win running variable equle to True
    def Run(self, Running=True):
        while Running:
            self.Play_Game()
            # allaw window to receive input from keyboard
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        Running = False

                    if event.key == K_LEFT:
                        self.snake.change_direction("left")

                    if event.key == K_RIGHT:
                        self.snake.change_direction("right")

                    if event.key == K_UP:
                        self.snake.change_direction("up")

                    if event.key == K_DOWN:
                        self.snake.change_direction("down")

                # when user want to exit window game
                elif event.type == QUIT:
                    Running = False

            time.sleep(.3)


if __name__ == '__main__':
    Game = Game_Window()
    Game.Run()
