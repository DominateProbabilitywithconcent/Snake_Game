import pygame,random
from copy import deepcopy
green = pygame.Color(0,255,0)
red = pygame.Color(255,0,0)
yellow = pygame.Color(255,255,0)
class Cell:
    def __init__(self,pos,cell_size):
        self.pos = pos
        self.cell_size = cell_size
        self.content = None
    def Draw(self):
        pass
class Food(Cell):
    def __init__(self, pos, cell_size,food_spawn):
        super().__init__(pos, cell_size)
        self.food_spawn = food_spawn
    def Draw(self, surface):
        if self.food_spawn == True:
            pygame.draw.rect(surface, red, pygame.Rect(self.pos[0], self.pos[1], self.cell_size, self.cell_size))
    def Spawn(self,snake):
        if self.food_spawn == False:
            for posX in snake.snake_pos:
                for posY in snake.snake_pos:
                    if self.pos[0] == posX and self.pos[1] == posY:
                        self.food_spawn = False
                        return False
                    else:
                        self.pos = [random.randrange(10, (850//10)) * 10, random.randrange(50, (550//10)) * 10]
                        self.food_spawn = True

        
class Snake:
    def __init__(self,snake_pos,snake_body,direction,cell_size):
        self.snake_pos = snake_pos
        self.snake_body = snake_body
        self.state = False
        self.is_dead = False
        self.direction = direction
        self.change_to = self.direction
        # self.snake = [[1 for _ in range(0,len(snake_body),cell_size)]for _ in range(1,len(snake_body),cell_size)]
    def Draw(self,surface):
        for pos in self.snake_body:
            pygame.draw.rect(surface, green, pygame.Rect(pos[0], pos[1], 10, 10))
    def Handle_event(self,event):
        if event.key == pygame.K_UP or event.key == ord('w'):
            self.change_to = 'UP'
        if event.key == pygame.K_DOWN or event.key == ord('s'):
            self.change_to = 'DOWN'
        if event.key == pygame.K_LEFT or event.key == ord('a'):
            self.change_to = 'LEFT'
        if event.key == pygame.K_RIGHT or event.key == ord('d'):
            self.change_to = 'RIGHT'        
    def Moving(self):
        if self.direction == 'UP':
            self.snake_pos[1] -= 10
        if self.direction == 'DOWN':
            self.snake_pos[1] += 10
        if self.direction == 'LEFT':
            self.snake_pos[0] -= 10
        if self.direction == 'RIGHT':
            self.snake_pos[0] += 10 
        self.snake_body.insert(0, list(self.snake_pos))
    def Set_direction(self):
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
    def Add_Length(self,food,game):
        if self.snake_pos[0] == food.pos[0] and self.snake_pos[1] == food.pos[1]:
            food.food_spawn = False
            game.score += 1
        else:
            self.snake_body.pop()
    def Is_dead(self,game):
        if self.is_dead == True:
            my_font = pygame.font.SysFont('times new roman', 90)
            game_over_surface = my_font.render('YOU DIED', True, red)
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (game.width_of_window/3, game.length_of_window/4)
            game.window.blit(game_over_surface, game_over_rect)
            game.show_score(0, red, 'times', 1)
            pygame.display.flip()
    def is_position_free(self, position,board):
        if position[0] >= board.width/board.cell_size or position[0] < 0 or position[1] >= board.length/board.cell_size or position[1] < 0:
            return False
        for pos in self.snake_body:
            if pos == position:
                return False
        return True
    def Game_over(self,game):
        if self.snake_pos[0] < 10 or self.snake_pos[0] > 850:
            self.is_dead = True
            game.state = False
            self.Is_dead(game)
        if self.snake_pos[1] < 50 or self.snake_pos[1] > 590:
            game.state = False
            self.is_dead = True
            self.Is_dead(game)
        for block in self.snake_body[1:]:
            if self.snake_pos[0] == block[0] and self.snake_pos[1] == block[1]:
                game.state = False
                self.is_dead = True
                self.Is_dead(game)