import pygame
import random
import sys
import numpy as np

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

GRIDSIZE = 40
GRID_WIDTH = int(SCREEN_HEIGHT / GRIDSIZE)
GRID_HEIGHT = int(SCREEN_WIDTH / GRIDSIZE)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

times_in = 0

class Snake(object):
    def __init__(self):
        self.snake_length = 1
        self.snake_positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.tail = (0, 0)

    def get_head_position(self):
        return self.snake_positions[0]

    def turn(self, point):
        if self.snake_length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*GRIDSIZE))), (cur[1] + (y*GRIDSIZE)))
        if (len(self.snake_positions) > 2 and new in self.snake_positions[2:-1]) or new[0] == -GRIDSIZE or new[1] == -GRIDSIZE or new[0] == SCREEN_WIDTH or new[1] == SCREEN_HEIGHT:
            self.reset()
            reset_grid()
            food.randomize_position()

        else:
            for i in self.snake_positions:
                grid[int(i[1] / GRIDSIZE), int(i[0] / GRIDSIZE)] = 1
            
            grid[int(new[1] / GRIDSIZE), int(new[0] / GRIDSIZE)] = 3
            
            if len(self.snake_positions) + 1 > self.snake_length:
                old = self.snake_positions.pop()
                grid[int(old[1] / GRIDSIZE), int(old[0] / GRIDSIZE)] = 0

            self.snake_positions.insert(0, new)
            grid[int(self.snake_positions[-1][1] / GRIDSIZE), int(self.snake_positions[-1][0] / GRIDSIZE)] = 4
            self.tail = self.snake_positions[-1]

    def reset(self):
        global score
        self.snake_length = 1
        self.snake_positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        score = 0
    
    def draw(self, surface):
        sprite = pygame.image.load("resources/snake.jpg").convert()
        for SnakeBody in self.snake_positions:
            surface.blit(sprite,(SnakeBody[0], SnakeBody[1]))

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    self.turn(UP)

                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)

                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)

                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

# -------------------- Class Food -------------------------------
class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = (114, 137, 218)
        self.randomize_position()

    def get_position(self):
        return self.position

    def randomize_position(self):
        grid[int(self.position[1]/GRIDSIZE), int(self.position[0]/GRIDSIZE)] = 0
        self.position = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)
        #if the 
        if self.position in snake.snake_positions:
            self.randomize_position() #recursive call

        grid[int(self.position[1]/GRIDSIZE), int(self.position[0]/GRIDSIZE)] = 2

    def draw(self, surface):
        Food_image = pygame.image.load("resources/food.jpg").convert()
        surface.blit(Food_image, (self.position[0], self.position[-1]))

    def get_position(self):
        return self.position

def drawGrid(surface, myfont):
    background = pygame.image.load("resources/background.jpg")
    surface.blit(background,(0,0))

# -------------------- Class Node -------------------------------
class Node():
    def __init__(self, position, parent = None):
        self.position = (int(position[0]), int(position[1]))
        #parent is the parent node
        self.parent = parent
    
    # Compare Nodes
    def __eq__(self, other):
        return self.position == other.position

    # Print Nodes
    def __repr__(self):
        return str(self.position)

    def get_parent(self):
        return self.parent

    def get_neighbors(self):
        #returns neighbors (UP, RIGHT, DOWN, LEFT)
        #THIS DOES NOT MEAN THE NEIGHBORING POSITIONS ARE not obstacles

        children = []
        for new_position in [UP, RIGHT, DOWN, LEFT]:

            node_position = (self.position[0] + new_position[0], self.position[1] + new_position[1])

            temp = self
            broken = False

            while temp is not None:
                if (temp.position == node_position):
                    broken = True
                    break

                temp = temp.parent

            if broken:
                continue

            if node_position[0] >= GRID_HEIGHT  or node_position[0] < 0 or node_position[1] >= GRID_HEIGHT  or node_position[1] < 0:
                continue

            if (grid[node_position[1], node_position[0]] == 1 or grid[node_position[1], node_position[0]] == 3 or (grid[node_position[1], node_position[0]] == 4)):
                continue

            new_node = Node(node_position, self)

            children.append(new_node)

        return children

    def on_grid(self):
        x = self.position[0]
        y = self.position[1]
        return (x >= GRID_WIDTH or x < 0 or y >= GRID_HEIGHT or y < 0)
    
    def is_snake_node(self, snake):
        x = self.position[0]
        y = self.position[1]
        
        for pos in snake.positions:
            if (pos[0] == x and pos[1] == y):
                return True
            
        return False
    
    def get_position(self):
        return self.position
    
    #this method traces through its parents and adds their positions to a list
    #order would be [1st gen node, 2nd gen node, ..., this node]
    def listify(self):
        list = []
        list.insert(0, self.position)

        node = self.parent
        while node is not None:
            list.insert(0, node.position)
            node = node.parent

        return list

def mult_node_is_obstacle(nodes):
        return_bools = []
        for node in nodes:
            return_bools.append(node.on_grid() and (not node.is_snake_node))
            
        return return_bools

# --------------------Depth First Search Algorithm -------------------------------
def dfs(start_pos, goal_pos):
    open_list = []
    closed_list = []

    start_node = Node(start_pos)
    goal_node = Node(goal_pos)

    open_list.append(start_node)

    while (len(open_list) != 0):
        cur_node = open_list.pop(-1)

        closed_list.append(cur_node)
        
        if (cur_node == goal_node):
            path = []
            while cur_node != start_node:
                path.append(cur_node.get_position())
                cur_node = cur_node.get_parent()
            # code before wouldnt insert start node into path so i added it here
            path.append(start_node.get_position())

            return path[::-1]

        cur_node_neighbors = cur_node.get_neighbors()
        #array to see if neighbors are obstacles
        #Checks to see if there are available nodes

        for child in cur_node_neighbors:
            #if the node isnt an obstacle and it isnt in the closed list then add it to the open list
            #adds child nodes to open list 
            if child in closed_list:
                continue

            if child not in open_list:
                open_list.insert(0, child)
    
    return None
                  
score = 0
grid = 0
def reset_grid():
    global grid
    grid = np.zeros((GRID_WIDTH, GRID_HEIGHT))
    grid = grid.astype(int)

reset_grid()
directions = []

def snake_directions(path):
    directions = []

    for i in range(len(path) - 1):
        direction_vector = (path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1])
        directions.insert(0,direction_vector)
    return directions

def dead():
    snake.reset()
    reset_grid()
    food.randomize_position()
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
food = 0
snake = 0
surface = 0
depth = 0
MAX_DEPTH = 0

def main():
    global score, food, snake, surface, simulated
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    myfont = pygame.font.SysFont("arial", 30)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface, myfont)

    snake = Snake()
    food = Food()

    while (True):
        
        clock.tick(15)
       
        
            
        if snake.get_head_position() == food.get_position():
            snake.snake_length += 1
            score = snake.snake_length - 1
            food.randomize_position()
    
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        screen.blit(surface, (0, 0))
        text = myfont.render("Score : {0}".format(score), 1, (255, 255, 255))
        screen.blit(text, (550, 10))
        
        drawGrid(surface, myfont)
        
        start_pos = (snake.get_head_position()[0]/GRIDSIZE, snake.get_head_position()[1]/GRIDSIZE)
        food_pos = (food.get_position()[0] / GRIDSIZE, food.get_position()[1]/GRIDSIZE)

     
        path = dfs(start_pos, food_pos)

        snake_dir = snake_directions(path).pop()


        snake.turn(snake_dir)

        snake.move()
      
         
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
          