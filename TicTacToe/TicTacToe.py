import pygame
import sys
import random
from board import Board
from numpy import *

class TicTacToe:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600,600))

        #Game stats
        self.board = Board(self)
        self.array = ['','','',
                      '','','',
                      '','','']

        self.player, self.computer = self.random_symbol()
        self.turn = self.random_turn()
        
        #Sound and font
        self.move = pygame.mixer.Sound('move.wav')
        self.font = pygame.font.SysFont('8-BIT WONDER', 150, bold = True)

    def run_game(self):
        '''Main loop'''
        while True:
            self.check_events()
            self.AI()
            self.game_over(self.player, self.computer)
            self.update_screen()
            
    def check_events(self):
        '''Take user input'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self, event):
        '''Take keypress input'''
        if event.key == pygame.K_r:
            self.reset(self.array)
        if self.turn == 'player':
            if event.key == pygame.K_KP1:
                self.make_player_move(self.array, self.player, 6)
            if event.key == pygame.K_KP2:
                self.make_player_move(self.array, self.player, 7)
            if event.key == pygame.K_KP3:
                self.make_player_move(self.array, self.player, 8)
            if event.key == pygame.K_KP4:
                self.make_player_move(self.array, self.player, 3)
            if event.key == pygame.K_KP5:
                self.make_player_move(self.array, self.player, 4)
            if event.key == pygame.K_KP6:
                self.make_player_move(self.array, self.player, 5)
            if event.key == pygame.K_KP7:
                self.make_player_move(self.array, self.player, 0)
            if event.key == pygame.K_KP8:
                self.make_player_move(self.array, self.player, 1)
            if event.key == pygame.K_KP9:
                self.make_player_move(self.array, self.player, 2)

    def draw_array(self, ar):
        '''Draw the moves on the screen'''
        newArr = [[ar[0],ar[1],ar[2]],[ar[3],ar[4],ar[5]],[ar[6],ar[7],ar[8]]]
        for i in range(3):
            for j in range(3):
                move = self.font.render(newArr[j][i], False, (0,0,0))
                self.screen.blit(move,(170+i*100,150+j*100))

    def random_turn(self):
        #Bug: return alway 0
        if random.randint(0,1) == 0:
            return 'player'
        else:
            return 'computer'

    def random_symbol(self):
        #Bug: return alway 0
        if random.randint(0,1) == 0:
            return 'x','o'
        else:
            return 'o','x'

    def make_move(self, array, player, index):
            array[index] = player

    def make_player_move(self, array, player, index):
        '''Make the player move if it is a legal one'''
        if self.isEmpty(array,index):
            self.make_move(array, player, index)
            self.turn = 'computer'
            pygame.mixer.Sound.play(self.move)

    def AI(self):
        '''Make the real computer move'''
        if self.turn == 'computer' and not self.isFull(self.array):
            index = self.make_computer_move(self.array)
            self.make_move(self.array, self.computer, index)
            self.turn = 'player'
            
    def make_computer_move(self,array):
        '''Return a move chose by computer'''
        # Make winning move if possible
        for i in range(9):
            copy = array.copy()
            if self.isEmpty(copy, i):
                self.make_move(copy,self.computer,i)
                if self.check_win(copy,self.computer):
                    return i

        # Block the player's winning move
        for i in range(9):
            copy = array.copy()
            if self.isEmpty(copy, i):
                self.make_move(copy,self.player,i)
                if self.check_win(copy,self.player):
                    return i

        # Take the center
        if self.isEmpty(copy,4):
            return 4

        # Take the corner
        corner = [0,2,6,8]
        random.shuffle(corner)
        for i in range(4):
            copy = array.copy()
            if self.isEmpty(copy, corner[i]):
                return corner[i]

        # Take the side
        sides = [1,3,5,7]
        random.shuffle(sides)
        for i in range(4):
            copy = array.copy()
            if self.isEmpty(copy, sides[i]):
                return sides[i]

    def reset(self, array):
        '''Clean the screen and reset the turn'''
        self.turn = self.random_turn()
        print(self.turn)
        self.board.end_message = self.board.font.render('', False, self.board.color)
        
        for i in range(9):
            self.make_move(array,'',i)

    def isEmpty(self, array, index):
        return array[index] == ''

    def isFull(self, array):
        if '' in array:
            return False
        else:
            return True

    def check_win(self, ar, le):
        return (
                # Orizontal
                (ar[0] == le and ar[1] == le and ar[2] == le) or
                (ar[3] == le and ar[4] == le and ar[5] == le) or
                (ar[6] == le and ar[7] == le and ar[8] == le) or

                # Vertical
                (ar[0] == le and ar[3] == le and ar[6] == le) or
                (ar[1] == le and ar[4] == le and ar[7] == le) or
                (ar[2] == le and ar[5] == le and ar[8] == le) or

                # Diagonal
                (ar[0] == le and ar[4] == le and ar[8] == le) or
                (ar[6] == le and ar[4] == le and ar[2] == le)
                )

    def game_over(self, player, computer):
        if self.check_win(self.array, computer):
            self.board.end_message = self.board.font.render('Game Over', False, self.board.color)
            self.turn = None
        if not self.check_win(self.array, computer) and self.isFull(self.array):
            self.board.end_message = self.board.font.render('      Tie', False, self.board.color)
            self.turn = None
        
    def update_screen(self):
        self.screen.fill((230,230,230))
        self.board.draw()
        self.draw_array(self.array)
        pygame.display.flip()


TTT = TicTacToe()
TTT.run_game()



