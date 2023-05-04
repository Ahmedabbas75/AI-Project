# import module we need in project
from pygame.locals import *
from Snake_Module import *
from Food_Module import *
import time

class Game_Window:
    def __init__(self):
        pygame.init()
        self.Window = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("AI Project")
        self.snake = Snake(self.Window,10)
        self.snake.Draw_Snake()
        self.food = Food(self.Window)
        self.food.Draw_Food()


    def Play_Game(self):
        self.snake.Snake_Walk()
        self.food.Draw_Food()
 
    # running window win running variable equle to True
    def Run(self, Running = True):
        while Running:
            # allaw window to receive input from keyboard
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        Running = False

                    if event.key == K_LEFT:
                        self.snake.Move_left()

                    if event.key == K_RIGHT:
                        self.snake.Move_right()

                    if event.key == K_UP:
                        self.snake.Move_up()

                    if event.key == K_DOWN:
                        self.snake.Move_down()
                 

                # when user want to exit window game
                elif event.type == QUIT:
                    Running = False
            
            self.Play_Game()
            time.sleep(.2)

if __name__ == '__main__':
    Game = Game_Window()
    Game.Run()


