import pygame,sys
class Button:
    def __init__(self,color ,x,y,width,length,text=' '):
        self.x = x
        self.y = y
        self.text = text 
        self.rect = pygame.Rect(x,y,width,length)
        self.color = color
        self.width = width
        self.length = length
        self.clicked = False
        self.visible = True
    def Is_clicked(self,event,mouse):
        if event.type == pygame.MOUSEBUTTONDOWN:
             if mouse[0] > self.x and mouse[0] < self.x + self.width:
                if mouse[1] > self.y and mouse[1] < self.y + self.length:
                    print(" ")
            
    def Draw(self,win,text):
        pygame.draw.rect(win,self.color,self.rect)
        if self.text != ' ':
            font = pygame.font.SysFont('Consolas',25)
            text = font.render(self.text,True,(0,0,0))
        win.blit(text,(self.x + (self.width/2 - text.get_width()/2), self.y + (self.length/2 - text.get_height()/2)))
class ExitButton(Button):
    def Is_clicked(self, event, mouse):
        if event.type == pygame.MOUSEBUTTONDOWN:
             if mouse[0] > self.x and mouse[0] < self.x + self.width:
                if mouse[1] > self.y and mouse[1] < self.y + self.length:
                    sys.exit()
class StartButton(Button):
    def Is_clicked(self, event, mouse,game):
        if event.type == pygame.MOUSEBUTTONDOWN:
             if mouse[0] > self.x and mouse[0] < self.x + self.width:
                if mouse[1] > self.y and mouse[1] < self.y + self.length:
                    game.state = 1
class ResetButton(Button):
    def Is_clicked(self, event, mouse,game,board,exit,start,reset,snake):
        if event.type == pygame.MOUSEBUTTONDOWN:
             if mouse[0] > self.x and mouse[0] < self.x + self.width:
                if mouse[1] > self.y and mouse[1] < self.y + self.length:
                    game.Reset(board,exit,start,reset,snake)
class BFSButton(Button):
    def Is_clicked(self, event, mouse,game):
        if event.type == pygame.MOUSEBUTTONDOWN:
             if mouse[0] > self.x and mouse[0] < self.x + self.width:
                if mouse[1] > self.y and mouse[1] < self.y + self.length:
                    game.state = 2
class DFSButton(Button):
    def Is_clicked(self, event, mouse,game):
        if event.type == pygame.MOUSEBUTTONDOWN:
             if mouse[0] > self.x and mouse[0] < self.x + self.width:
                if mouse[1] > self.y and mouse[1] < self.y + self.length:
                    game.state = 3
class AStarButton(Button):
    def Is_clicked(self, event, mouse,game):
        if event.type == pygame.MOUSEBUTTONDOWN:
             if mouse[0] > self.x and mouse[0] < self.x + self.width:
                if mouse[1] > self.y and mouse[1] < self.y + self.length:
                    game.state = 4
                    

                    
    
    