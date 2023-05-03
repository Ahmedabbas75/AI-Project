# import module we need in project
import pygame
from pygame.locals import *

# class snake style
class Snake:
    def __init__(self, Screen):
        self.parent_screen = Screen
        self.SnakeHead = pygame.image.load("resources/block.jpg").convert()
        self.Snake_pos_X = 100 # X coordinate of initial position
        self.Snake_pos_Y = 100 # Y coordinate of initial position
        
    # set new position of the snake head base on left direction
    def Move_left(self):
        self.Snake_pos_X -= 10
        self.Draw()

    # set new position of the snake head base on right direction
    def Move_right(self):
        self.Snake_pos_X += 10
        self.Draw()

    # set new position of the snake head base on up direction
    def Move_up(self):
        self.Snake_pos_Y -= 10
        self.Draw()

    # set new position of the snake head base on down direction
    def Move_down(self):
        self.Snake_pos_Y += 10
        self.Draw()

    # update head of snake
    def Draw(self):
        self.parent_screen.fill((110, 110, 5))
        self.parent_screen.blit(self.SnakeHead,(self.Snake_pos_X,self.Snake_pos_Y))
        pygame.display.flip() # allow changes to occur


class Game_Window:
    def __init__(self):
        pygame.init()
        self.Window = pygame.display.set_mode((500, 500))
        self.snake = Snake(self.Window)
        self.snake.Draw()
    
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

if __name__ == '__main__':
    Game = Game_Window()
    Game.Run()


