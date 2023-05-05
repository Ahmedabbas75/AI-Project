# import module we need in project
import pygame
from Snake_Module import *
from Food_Module import *

class GameWindow:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("AI Project")
        self.snake = Snake(self.window,2)
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
    def check_ate_food(self):
        return [self.snake.snake_pos_x[0], self.snake.snake_pos_y[0]] == self.food.Food_pos
         

    def Play_Game(self):
        pygame.display.update()
        self.window.fill((110, 110, 5))
        self.clock.tick(60)
        self.time_update()
        self.display_score()

        if self.check_ate_food():
            self.snake.increase_Snake_lenght()
            self.food.Move_food()

        self.snake.is_collision()
        self.food.Draw_Food()
        self.snake.Draw_Snake()


        

    def display_score(self):
        self.window.fill((110, 110, 5))
        font_style = pygame.font.SysFont("Arial",30)
        score = font_style.render(f"Score: {self.snake.Snake_length - 1}",True, (255,255,255))
        self.window.blit(score,(700,10))

    def over_game(self):
        font = pygame.font.SysFont('arial', 30)
        font_style1 = font.render(f"Game is over! Your score is {self.snake.Snake_length - 1}", True, (255, 255, 255))
        self.window.blit(font_style1, (200, 200))
        font_style2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.window.blit(font_style2, (200, 300))
        pygame.display.update()



    # running window win running variable equle to True
    def Run(self, running = True, pause = False):
        while running:
            # allaw window to receive input from keyboard
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

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
                    running = False
            
            try:
                if not pause:
                    self.Play_Game()
            
            except Exception as e:
                self.over_game()
                pause = True
        



if __name__ == '__main__':
    Game = GameWindow()
    Game.Run()
