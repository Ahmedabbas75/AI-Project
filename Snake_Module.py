# import module we need in project
import pygame

class Snake:
    def __init__(self, Screen, Snake_length):
        self.SnakeHead = pygame.image.load("resources/snake.jpg").convert()
        self.Snake_length = Snake_length
        self.parent_screen = Screen
        self.Direction = "right"
        self.sizes_head = 40

        # set X,Y coordinates of initial position to snake
        self.snake_pos_x, self.snake_pos_y = ([self.sizes_head] * Snake_length), ([self.sizes_head] * Snake_length)
    
    def get_Snake_length(self):
        return self.Snake_length

    def increase_Snake_lenght(self):
        self.Snake_length += 1
        self.snake_pos_x.append(self.snake_pos_x[-1])
        self.snake_pos_y.append(self.snake_pos_y[-1])

    # set new position of the snake head base on direction
    def change_direction(self, new_direction):
        self.Direction = new_direction

    def get_snake_pos(self):
        return [self.snake_pos_x,self.snake_pos_y]

    # update head of snake
    def Draw_Snake(self):
        for index in range(self.Snake_length):
            self.parent_screen.blit(self.SnakeHead,(self.snake_pos_x[index], self.snake_pos_y[index]))

    def Snake_Walk(self):
        # update head of snake
        if self.Direction == "left":
            self.snake_pos_x[0] -= self.sizes_head

        if self.Direction == "right":
            self.snake_pos_x[0] += self.sizes_head

        if self.Direction == "up":
            self.snake_pos_y[0] -= self.sizes_head

        if self.Direction == "down":
            self.snake_pos_y[0] += self.sizes_head

        # update body and tail of snake
        for index_body in range(self.Snake_length-1, 0, -1):
            self.snake_pos_x[index_body] = self.snake_pos_x[index_body - 1]
            self.snake_pos_y[index_body] = self.snake_pos_y[index_body - 1]

    # check snake colliding itself or frame
    def check_colliding(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + self.sizes_head:
            if y1 >= y2 and y1 < y2 + self.sizes_head:
                return True
        return False
    
    
    def is_collision(self):
        for check_index in range(3,self.Snake_length):
            if self.check_colliding(self.snake_pos_x[0],self.snake_pos_y[0],
                        self.snake_pos_x[check_index],self.snake_pos_y[check_index]):
                raise "Game over"
            