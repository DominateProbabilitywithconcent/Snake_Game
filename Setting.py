import pygame

 # Gap between adjacent squares


icon = pygame.image.load('Changeling.png')
cyan = pygame.Color(176,224,230)
black = pygame.Color(0,0,0)
green =pygame.Color(0,255,0)
red = pygame.Color(255,0,0)
white = pygame.Color(255,255,255)
grey = pygame.Color(128, 128, 128)

SNAKE_CLR = green
APPLE_CLR = red
HEAD_CLR = (0,150,0)
width_of_window, length_of_window = 1300, 700
width_of_board, length_of_board = 800,500
ROWS = 25   
COLUMNS = 40
SQUARE_SIZE = 10
GAP_SIZE = 2
VIRTUAL_SNAKE_CLR = black
difficulty = 60

INITIAL_SNAKE_LENGTH = 3
MAX_MOVES_WITHOUT_EATING = COLUMNS * ROWS * ROWS * 2  
SNAKE_MAX_LENGTH = COLUMNS * ROWS - INITIAL_SNAKE_LENGTH  

GRID = [[i, j] for i in range(1,COLUMNS*2+2) for j in range(4,ROWS*2+6)]


# Helper functions
def get_neighbors(position):
    neighbors = [[position[0] + 1, position[1]],
                 [position[0] - 1, position[1]],
                 [position[0], position[1] + 1],
                 [position[0], position[1] - 1]]
    in_grid_neighbors = []
    for pos in neighbors:
        if pos in GRID:
            in_grid_neighbors.append(pos)
    return in_grid_neighbors

def distance(pos1, pos2):
    x1, x2 = pos1[0], pos2[0]
    y1, y2 = pos1[1], pos2[1]
    return abs(x2 - x1) + abs(y2 - y1)

ADJACENCY_DICT = {tuple(pos): get_neighbors(pos) for pos in GRID}
