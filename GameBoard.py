import pygame
grey = pygame.Color(128, 128, 128)
black = pygame.Color(0,0,0)
class Game_Board:
    def __init__(self,surface,width, length,cell_size):
        self.width = width
        self.length = length
        self.cell_size = cell_size
        self.surface = surface
        self.board = [[0 for _ in range(0,width,cell_size)]for _ in range(1,length,cell_size)]
    def State_change(self):
        
    def draw_grid(self, horizontal_initial_point, vertical_initial_point,color):
        for r in range(0,self.width,self.cell_size):
            horizontal_initial_point = horizontal_initial_point + 10
            pygame.draw.line(self.surface, color, (horizontal_initial_point, 50), (horizontal_initial_point, self.length+50))
        for n in range(0,self.length,self.cell_size):
            vertical_initial_point = vertical_initial_point + 10
            pygame.draw.line(self.surface, color, (10, vertical_initial_point), (self.width+10, vertical_initial_point))
    def draw_Board(self):
        pygame.draw.rect(self.surface,black,pygame.Rect(10,50,self.width,self.length))

            
        

        