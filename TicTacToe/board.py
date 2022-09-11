import pygame

class Board:
    def __init__(self,game):
        self.screen = game.screen
        self.color = (0,0,0)
        self.font = pygame.font.SysFont('8-BIT WONDER', 70, bold = True)
        self.font2 = pygame.font.SysFont('8-BIT WONDER', 30)
        
        self.title = self.font.render('TicTacToe', False, self.color)
        self.rules = self.font2.render('Use Numpad to make your move', False, self.color)
        self.rules2 = self.font2.render('or press R to reset', False, self.color)
        self.end_message = self.font.render('', False, self.color)

    def draw(self):
        self.screen.blit(self.title,(160,50))
        self.screen.blit(self.rules,(125,100))
        self.screen.blit(self.rules2,(200,120))
        self.screen.blit(self.end_message,(150,500))
        
        pygame.draw.line(self.screen,self.color,(250,150),(250,450),5)
        pygame.draw.line(self.screen,self.color,(350,150),(350,450),5)

        pygame.draw.line(self.screen,self.color,(150,250),(450,250),5)
        pygame.draw.line(self.screen,self.color,(150,350),(450,350),5)
    
        
