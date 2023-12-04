import pygame, sys, time, random
from Button import *
from GameBoard import *
#Initialize game
pygame.init()
pygame.display.set_caption('Snake Hunt') #caption
Icon = pygame.image.load('Changeling.png')
pygame.display.set_icon(Icon)
#difficulty
difficulty = 15
#Colors
cyan = pygame.Color(176,224,230)
black = pygame.Color(0,0,0)
green =pygame.Color(0,255,0)
red = pygame.Color(255,0,0)
white = pygame.Color(255,255,255)
grey = pygame.Color(128, 128, 128)

#Size of window
width_of_window, height_of_window = 1300, 700
screen = pygame.display.set_mode((width_of_window, height_of_window))
play_surface = pygame.draw.rect(screen, black,pygame.Rect(10,50,850,550))
fps_controller = pygame.time.Clock()
#Snake
class Snake:
    def __init__(self,snake_pos,snake_body):
        self.snake_pos = snake_pos
        self.snake_body = snake_body
        self.state = False
        self.is_dead = False
        self.dir = 'RIGHT'
    def Add_Length(self):
        for pos in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            snake_body.pop()
    def Is_dead(self):
        if self.is_dead == True:
            my_font = pygame.font.SysFont('times new roman', 90)
            game_over_surface = my_font.render('YOU DIED', True, red)
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (width_of_window/3, height_of_window/4)
            screen.blit(game_over_surface, game_over_rect)
            show_score(0, red, 'times', 1)
            pygame.display.flip()
    def Game_over(self):
        if snake_pos[0] < 10 or snake_pos[0] > 850:
            self.is_dead = True
            self.state = False
            self.Is_dead()
        if snake_pos[1] < 50 or snake_pos[1] > 590:
            self.state = False
            self.is_dead = True
            self.Is_dead()
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                self.state = False
                self.is_dead = True
                self.Is_dead()
                



head1 = random.randrange(10, (850//10))*10
head2 = random.randrange(50, (550//10)) * 10
snake_pos = [head1,head2]
snake_body = [[head1,head2],[head1-10,head2],[head1-(2*10),head2]]
snake1 = Snake(snake_pos, snake_body)
#Food 
class Food:
    def __init__(self,food_pos, food_spawn):
        self.food_pos = food_pos
        self.food_spawn = food_spawn
    def draw(self):
        pygame.draw.rect(screen, red, pygame.Rect(self.food_pos[0], self.food_pos[1], 10, 10))
    def spawn(self):
        if self.food_spawn is False:
            self.food_pos = [random.randrange(10, (850//10)) * 10, random.randrange(50, (550//10)) * 10]
        
food_pos = [random.randrange(10, (850//10)) * 10, random.randrange(50, (550//10)) * 10]
food_spawn = True
food1 = Food(food_pos,food_spawn)
# class Obstacle:
#     def __init__(self, obstacle_pos):
#         self.obstacle_pos = obstacle_pos
#     def draw(self):
#         pygame.draw.rect(screen,grey,pygame.Rect(self.obstacle_pos[0],self.obstacle_pos[1],10,10))
#     def put
direction = 'RIGHT'
change_to = direction
score = 0
#Button

     
display_color = red

screen.fill(cyan)
exitButton = Button(red,1000,500,200,100,"Quit")
SinglePlayerButton = Button(display_color,1000,200,200,100,"Single Player")
MonoBotButton = Button(red,1000,350,200,100,"Single Bot")


        
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (width_of_window/10, 15)
    else:
        score_rect.midtop = (width_of_window/2, height_of_window/1.25)
    screen.blit(score_surface, score_rect)
    # pygame.display.flip()
#Running the game
running = True
screen.fill(cyan)
exitButton.Draw(screen,"")
SinglePlayerButton.Draw(screen,"")
MonoBotButton.Draw(screen,"")
play_surface = pygame.draw.rect(screen, black,pygame.Rect(10,50,850,550))
show_score(1,black,'times new roman',25)
snake1.Add_Length()
gameBoard = Game_Board(screen,850,550,10)
while running:
    gameBoard.draw_grid(0,50,red)
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right  
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
        mouse = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #single player button
            if mouse[0] > 1000 and mouse[0] < 1000 + 120:
                if mouse[1] > 200 and mouse[1] < 200 + 100:
                            snake1.state = True
                                
            #quit button
            if mouse[0] > 1000 and mouse[0] < 1000 + 120:
                if mouse[1] > 500 and mouse[1] < 500 + 100:
                               running = False
            
                        
        
    


    if snake1.state == True:
        # screen.fill(cyan)
        # exitButton.Draw(screen,"")
        # SinglePlayerButton.Draw(screen,"")
        # MonoBotButton.Draw(screen,"")
        # show_score(1,black,'times new roman',25)
        # play_surface = pygame.draw.rect(screen, black,pygame.Rect(10,50,850,550))
        # gameBoard.draw_grid(0,50,red)
        if direction == 'UP':
           snake1.snake_pos[1] -= 10
        if direction == 'DOWN':
            snake1.snake_pos[1] += 10
        if direction == 'LEFT':
            snake1.snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake1.snake_pos[0] += 10
        snake1.snake_body.insert(0  , list(snake_pos))
        if snake1.snake_pos[0] == food1.food_pos[0] and snake1.snake_pos[1] == food1.food_pos[1]:
            score += 1
            food1.food_spawn = False
        else:
            snake1.snake_body.pop()
        
        food1.spawn()
        food1.food_spawn = True
        #Draw snake body
        snake1.Add_Length()
        
        food1.draw()
        snake1.Game_over()
        
    pygame.display.update()
    fps_controller.tick(difficulty)

            