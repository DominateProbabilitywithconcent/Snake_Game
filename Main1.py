from re import S
import pygame, random,sys
from GameBoard import *
from Button import *
from Snake import *
from Setting import *
from BFS import *
class Game:
    def __init__(self,width_of_window,length_of_window,color):
        self.width_of_window = width_of_window
        self.length_of_window = length_of_window
        self.fps_controller = pygame.time.Clock()
        self.running = True
        self.state = -1
        self.window =  pygame.display.set_mode((self.width_of_window, self.length_of_window))
        self.color = color
    def Initialize_game(self,icon):
        pygame.init()
        pygame.display.set_caption('Snake Hunt') #caption
        pygame.display.set_icon(icon)
        
    def show_score(self,choice, color, font, size,snake):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(snake.score), True, color)
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
        self.window.fill(cyan)
        self.score = 0
        self.show_score(1,black,'Time New Roman',50,snake)
        board.draw_Board()
        board.draw_grid(10,50,grey)
        exit.Draw(self.window," ")
        start.Draw(self.window," ")
        reset.Draw(self.window," ")
        BFSbutton.Draw(Snake_Game.window," ")
        DFSbutton.Draw(Snake_Game.window," ")
        snake.__init__(self.window)
        snake.score = 0
        snake.squares_start_pos = [[COLUMNS // 2 + i, ROWS // 2] for i in range(INITIAL_SNAKE_LENGTH)]
        snake.apple = Square([randrange(COLUMNS), randrange(ROWS)], self.window, is_apple=True)
        snake.moves_without_eating = 0
        snake.is_dead = False
        snake.turns = {}
        snake.dir = [-1, 0]
        snake.is_virtual_snake = False
        snake.total_moves = 0
        self.state = 0



ADJACENCY_DICT = {tuple(pos): get_neighbors(pos) for pos in GRID}
Snake_Game = Game(width_of_window,length_of_window,cyan)
GameBoard = Game_Board(Snake_Game.window,width_of_board,length_of_board,SQUARE_SIZE)
snake = Snake(Snake_Game.window)
snake_2 = Snake(Snake_Game.window)
exitButton = ExitButton(red,1000,550,200,50,"Quit")
resetButton = ResetButton(red,1000,450,200,50,"Reset")
startButton = StartButton(red,1000,50,200,50,"Start")
BFSbutton = BFSButton(red,1000,150,200,50,"BFS")
DFSbutton = DFSButton(red,1000,250,200,50,"DFS")
Snake_Game.Initialize_game(icon)
Snake_Game.window.fill(Snake_Game.color)
GameBoard.draw_Board()
GameBoard.draw_grid(10,50,grey)
exitButton.Draw(Snake_Game.window," ")
resetButton.Draw(Snake_Game.window," ")
BFSbutton.Draw(Snake_Game.window," ")
DFSbutton.Draw(Snake_Game.window," ")
startButton.Draw(Snake_Game.window," ")
while Snake_Game.running == True:
    events =  pygame.event.get()
    mouse = pygame.mouse.get_pos()
    

    for event in events:
        if event.type == pygame.QUIT:
            Snake_Game.running = False
        snake.handle_events()
        exitButton.Is_clicked(event,mouse)
        startButton.Is_clicked(event,mouse,Snake_Game)
        resetButton.Is_clicked(event,mouse,Snake_Game,GameBoard,exitButton,startButton,resetButton,snake)
        BFSbutton.Is_clicked(event,mouse,Snake_Game)
        DFSbutton.Is_clicked(event,mouse,Snake_Game)
    if Snake_Game.state == 1:
        Snake_Game.window.fill(cyan)
        Snake_Game.show_score(1,black,'Time New Roman',50,snake)
        GameBoard.draw_Board()
        GameBoard.draw_grid(10,50,grey)
        exitButton.Draw(Snake_Game.window," ")
        BFSbutton.Draw(Snake_Game.window," ")
        DFSbutton.Draw(Snake_Game.window," ")
        resetButton.Draw(Snake_Game.window," ")
        startButton.Draw(Snake_Game.window," ")
        snake.update(Snake_Game)
    elif Snake_Game.state == 2:
        Snake_Game.window.fill(cyan)
        Snake_Game.show_score(1,black,'Time New Roman',50,snake)
        GameBoard.draw_Board()
        GameBoard.draw_grid(10,50,grey)
        exitButton.Draw(Snake_Game.window," ")
        BFSbutton.Draw(Snake_Game.window," ")
        DFSbutton.Draw(Snake_Game.window," ")
        resetButton.Draw(Snake_Game.window," ")
        startButton.Draw(Snake_Game.window," ")
        snake.BFSupdate(Snake_Game)
    elif Snake_Game.state == 3:
        Snake_Game.window.fill(cyan)
        Snake_Game.show_score(1,black,'Time New Roman',50,snake)
        GameBoard.draw_Board()
        GameBoard.draw_grid(10,50,grey)
        exitButton.Draw(Snake_Game.window," ")
        BFSbutton.Draw(Snake_Game.window," ")
        DFSbutton.Draw(Snake_Game.window," ")
        resetButton.Draw(Snake_Game.window," ")
        startButton.Draw(Snake_Game.window," ")
        snake.DFSupdate(Snake_Game)
    pygame.display.update()
    Snake_Game.fps_controller.tick(difficulty)