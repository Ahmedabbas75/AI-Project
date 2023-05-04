# import module we need in project
import pygame
from pygame.locals import *

# class snake style
class Snake:
    def __init__(self, Screen,Snake_length):
        self.SnakeHead = pygame.image.load("resources/block.jpg").convert()
        self.Snake_length = Snake_length
        self.parent_screen = Screen
        self.Direction = "right"
        self.SizeSnakeHead = 40

        # set X,Y coordinates of initial position to snake      
        self.Snake_pos_X, self.Snake_pos_Y = ([self.SizeSnakeHead] * Snake_length), ([self.SizeSnakeHead] * Snake_length)

    # set new position of the snake head base on left direction
    def Move_left(self):
       self.Direction = "left"

    # set new position of the snake head base on right direction
    def Move_right(self):
        self.Direction = "right"

    # set new position of the snake head base on up direction
    def Move_up(self):
       self.Direction = "up"

    # set new position of the snake head base on down direction
    def Move_down(self):
        self.Direction = "down"

    # update head of snake
    def Draw_Snake(self):
        self.parent_screen.fill((110, 110, 5))
        for index in range(self.Snake_length):
            self.parent_screen.blit(self.SnakeHead,(self.Snake_pos_X[index],self.Snake_pos_Y[index]))
        pygame.display.flip() # allow changes to occur


    def Snake_Walk(self):
        # update head of snake
        if self.Direction == "left":
            self.Snake_pos_X[0] -=self.SizeSnakeHead

        if self.Direction == "right":
            self.Snake_pos_X[0] +=self.SizeSnakeHead

        if self.Direction == "up":
            self.Snake_pos_Y[0] -=self.SizeSnakeHead

        if self.Direction == "down":
            self.Snake_pos_Y[0] +=self.SizeSnakeHead

        # update body and tail of snake
        for index_body in range(self.Snake_length-1,0,-1):
            self.Snake_pos_X[index_body] = self.Snake_pos_X[index_body - 1]
            self.Snake_pos_Y[index_body] = self.Snake_pos_Y[index_body - 1]
        
        self.Draw_Snake()

    