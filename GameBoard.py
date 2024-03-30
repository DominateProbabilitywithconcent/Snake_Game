import pygame
grey = pygame.Color(128, 128, 128)
black = pygame.Color(0,0,0)
class Game_Board:
    def __init__(self,surface,width, length,cell_size):
        self.width = width
        self.length = length
        self.cell_size = cell_size
        self.surface = surface  
    def draw_grid(self, init_x_point, init_y_point,color):
        for r in range(0,self.width,self.cell_size):
            init_x_point = init_x_point + self.cell_size
            pygame.draw.line(self.surface, color, (init_x_point, 60), (init_x_point, self.length+60))
        for n in range(0,self.length,self.cell_size):
            init_y_point = init_y_point + self.cell_size
            pygame.draw.line(self.surface, color, (10, init_y_point), (self.width+10, init_y_point))
    def draw_Board(self):
        pygame.draw.rect(self.surface,black,pygame.Rect(10,60,self.width,self.length))

            
        

        