from re import S
import pygame, random,sys
from GameBoard import *
from Button import *
from Snake import *
class Game:
    def __init__(self,width_of_window,length_of_window,color):
        self.width_of_window = width_of_window
        self.length_of_window = length_of_window
        self.fps_controller = pygame.time.Clock()
        self.running = True
        self.state = False
        self.window =  pygame.display.set_mode((self.width_of_window, self.length_of_window))
        self.color = color
        self.score = 0
    def Initialize_game(self,icon):
        pygame.init()
        pygame.display.set_caption('Snake Hunt') #caption
        pygame.display.set_icon(icon)
        
    def show_score(self,choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(self.score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (self.width_of_window/10, 15)
        else:
            
            score_rect.midtop = (self.width_of_window/2, self.length_of_window/1.25)
        self.window.blit(score_surface, score_rect)
        # pygame.display.update()
    def Change_game_speed(self,speed):
        self.fps_controller.tick(speed)
    def Reset(self,board,exit,start,reset,snake):
        head1 = random.randrange(5, (850//10))*10
        head2 = random.randrange(5, (550//10))* 10
        self.window.fill(cyan)
        self.score = 0
        self.show_score(1,black,'Time New Roman',50)
        board.draw_Board()
        board.draw_grid(0,50,grey)
        exit.Draw(self.window," ")
        start.Draw(self.window," ")
        reset.Draw(self.window," ")
        snake.snake_pos = [head1,head2]
        snake.snake_body = [[head1,head2],[head1-10,head2],[head1-(2*10),head2]]
        snake.Draw(self.window)
        self.state = False

width_of_window, length_of_window = 1300, 700
width_of_board, length_of_board = 850,550
icon = pygame.image.load('Changeling.png')
cyan = pygame.Color(176,224,230)
black = pygame.Color(0,0,0)
green =pygame.Color(0,255,0)
red = pygame.Color(255,0,0)
white = pygame.Color(255,255,255)
grey = pygame.Color(128, 128, 128)
head1 = random.randrange(5, (850//10))*10
head2 = random.randrange(5, (550//10))* 10
cell_size = 10
grid_width = 85
grid_height = 55
snake_pos = [head1,head2]
snake_body = [[head1,head2],[head1-10,head2],[head1-(2*10),head2]]
food_pos = [random.randrange(5, (850//10)) * 10, random.randrange(5, (550//10)) * 10]
food_spawn = True
direction = 'RIGHT'
change_to = direction
difficulty = 15

Snake_Game = Game(width_of_window,length_of_window,cyan)
GameBoard = Game_Board(Snake_Game.window,width_of_board,length_of_board,cell_size)
snake = Snake(snake_pos,snake_body,direction,cell_size)
food = Food(food_pos,cell_size,food_spawn)
exitButton = ExitButton(red,1000,500,200,100,"Quit")
resetButton = ResetButton(red,1000,350,200,100,"Reset")
startButton = StartButton(red,1000,50,200,100,"Start")
Snake_Game.Initialize_game(icon)
Snake_Game.window.fill(Snake_Game.color)
GameBoard.draw_Board()
GameBoard.draw_grid(0,50,grey)
exitButton.Draw(Snake_Game.window," ")
resetButton.Draw(Snake_Game.window," ")
startButton.Draw(Snake_Game.window," ")
snake.Draw(Snake_Game.window)
while Snake_Game.running == True:
    events =  pygame.event.get()
    mouse = pygame.mouse.get_pos()
    
    snake.Set_direction()
    for event in events:
        if event.type == pygame.QUIT:
            Snake_Game.running = False
        if event.type == pygame.KEYDOWN:
            snake.Handle_event(event)
        exitButton.Is_clicked(event,mouse)
        startButton.Is_clicked(event,mouse,Snake_Game)
        resetButton.Is_clicked(event,mouse,Snake_Game,GameBoard,exitButton,startButton,resetButton,snake)
    if Snake_Game.state == True:
        Snake_Game.window.fill(cyan)
        Snake_Game.show_score(1,black,'Time New Roman',50)
        GameBoard.draw_Board()
        GameBoard.draw_grid(0,50,grey)
        exitButton.Draw(Snake_Game.window," ")
        resetButton.Draw(Snake_Game.window," ")
        startButton.Draw(Snake_Game.window," ")
        snake.Draw(Snake_Game.window)
        snake.Moving()
        snake.Add_Length(food,Snake_Game)
        food.Spawn(snake)
        # food.food_spawn = True
        food.Draw(Snake_Game.window)
        snake.Game_over(Snake_Game)
    pygame.display.update()
    Snake_Game.fps_controller.tick(difficulty)