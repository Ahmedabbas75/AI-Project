# import module we need in project
import pygame

class Snake:
    def __init__(self, Screen, Snake_length):
        self.SnakeHead = pygame.image.load("resources/block.jpg").convert()
        self.Snake_length = Snake_length
        self.parent_screen = Screen
        self.Direction = "right"
        self.SizeSnakeHead = 40

        # set X,Y coordinates of initial position to snake
        self.Snake_pos_X, self.Snake_pos_Y = ([self.SizeSnakeHead] * Snake_length), ([self.SizeSnakeHead] * Snake_length)

    def increase_Snake_lenght(self):
        self.Snake_length += 1
        self.Snake_pos_X.append(self.Snake_pos_X[-1])
        self.Snake_pos_Y.append(self.Snake_pos_Y[-1])

    # set new position of the snake head base on direction
    def change_direction(self, new_direction):
        self.Direction = new_direction

    # update head of snake
    def Draw_Snake(self):
        for index in range(self.Snake_length):
            self.parent_screen.blit(
                self.SnakeHead, (self.Snake_pos_X[index], self.Snake_pos_Y[index]))

    def Snake_Walk(self):
        # update head of snake
        if self.Direction == "left":
            self.Snake_pos_X[0] -= self.SizeSnakeHead

        if self.Direction == "right":
            self.Snake_pos_X[0] += self.SizeSnakeHead

        if self.Direction == "up":
            self.Snake_pos_Y[0] -= self.SizeSnakeHead

        if self.Direction == "down":
            self.Snake_pos_Y[0] += self.SizeSnakeHead

        # update body and tail of snake
        for index_body in range(self.Snake_length-1, 0, -1):
            self.Snake_pos_X[index_body] = self.Snake_pos_X[index_body - 1]
            self.Snake_pos_Y[index_body] = self.Snake_pos_Y[index_body - 1]

 
            

