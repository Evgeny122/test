from encodings import CodecRegistryError
from textwrap import fill
from tkinter import *
from unittest import removeResult
# нужно вренуться и убрать импорт звезд
CANVAS_SIZE = 600
FIGURE_SIZE = 200
RATIO = CANVAS_SIZE // FIGURE_SIZE
BG_COLOR = 'black'
EMPTY = None
coords = 0
# Players setup
X = 'player 1'
O = 'player 2'
FIRST_PLAYER = X

class Board(Tk):
    def __init__(self, start_player):
        super().__init__()
        self.coords = coords
        self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE, bg=BG_COLOR)
        self.canvas.pack()
        self.figure_size = FIGURE_SIZE
        self.current_player = start_player
        self.canvas.bind('<Button-1>', self.click_event)
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    def build_grid(self, grid_color):
        line = RATIO - 1
        start_x = 0
        start_y = 0
        for i in range(line):
            start_x += FIGURE_SIZE
            start_y += FIGURE_SIZE
            self.canvas.create_line(start_x, 0, start_x, CANVAS_SIZE, fill=grid_color)
            self.canvas.create_line(0, start_y, CANVAS_SIZE, start_y, fill=grid_color)
        
    def render_cross(self, posX, posY):
        f_size = self.figure_size
        
        self.canvas.create_line(posX, posY, f_size + posX, f_size + posY, fill='red')
        self.canvas.create_line(f_size + posX, posY, posX, f_size + posY, fill='red')
    def render_circle(self, posX, posY):
        f_size = self.figure_size

        self.canvas.create_oval(posX, posY, posX + f_size, posY + f_size, outline='green', width=5)
        
    def winner(self, player=None):
        center = CANVAS_SIZE // 2
        if player:
            text = f'Winner: {player}'
        else:
            text = 'Draw'
        self.canvas.create_text(center, center, text=text, fill='white', font='Arial 50')
        self.canvas.unbind('<Button-1>')

        
    def click_event(self, event):
        self.event = event
        x_coord = event.x // FIGURE_SIZE
        y_coord = event.y // FIGURE_SIZE
        self.make_move(x_coord, y_coord)
        print(event.x, event.y)
        
        print(x_coord, y_coord)
       
    
    def make_move(self, x, y):
        d = {}
        for i in range(len(self.board)):
            d[i] = FIGURE_SIZE * i
        
        current_player = self.current_player

        if self.board[x][y] == EMPTY:
            self.update_board(x, y)

    def update_board(self, x, y):
        c_player = self.current_player
        self.board[x][y] = c_player
        print(self.board)
        if self.check_win(self.board, c_player):
            self.winner(c_player)
            self.win_line(self.event.x , self.event.y)
        elif self.check_draw(self.board):
            self.winner()
    
    def win_line(self, x, y):
        if self.coords == 1:
            if y <= 200:
                self.canvas.create_line(0, 100, 600, 100, fill='green')
            elif y <= 400 and y > 200:
                self.canvas.create_line(0, 300, 600, 300, fill='green')
            elif y <= 600 and y > 400:
                self.canvas.create_line(0, 500, 600, 500, fill='green')
        if self.coords == 2:
            if x <= 200:
                self.canvas.create_line(100, 0, 100, 600, fill='green')
            elif x <= 400 and x > 200:
                self.canvas.create_line(300, 0, 300, 600, fill='green')
            elif x <= 600 and x > 400:
                self.canvas.create_line(500, 0, 500, 600, fill='green')
        if self.coords == 3:
            self.canvas.create_line(0, 0, 600, 600, fill='green')
        if self.coords == 4:
            self.canvas.create_line(600, 0, 0, 600, fill='green')
            


    
        
        
    
    def check_win(self, board, player):
        '''список строятся вертикально'''
        s = [player]
        s = s * len(board)
        '''счетчик слева-направо'''
        timer_left_right = 0
        '''счетчик справа-налево'''

        timer_right_left = 0
        timer = [0, 1, 2]
        timer2 = [2, 1, 0]
        
        '''вертикальная проверка'''
        for i in board:
            if i == s:
                self.coords += 2
                return True

        '''горизонтальная проверка'''
        for i in range(len(board)):
            if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                self.coords += 1
                return True
        
        '''проверка по диагонале справа-налево'''
        for i in range(3):
            if board[i][i] != player:
                False
            else:
                timer_left_right += 1
                if timer_left_right == 3:
                    self.coords += 3
                    return True

        '''проверка по диагонале слева-направо'''                     
        for i in range(3):
            if board[timer2[i]][timer[i]] != player:
                False
            else:
                timer_right_left += 1
                if timer_right_left == 3:
                    self.coords += 4
                    return True
                

                    
        
                    
    def check_draw(self, board):
        pass





        




        


game_v1 = Board(start_player=FIRST_PLAYER)
game_v1.build_grid('red')




game_v1.mainloop()