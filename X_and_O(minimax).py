from tkinter import *
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
list_pl = [X, O]
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
        self.game_status = True
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
        self.game_status = False
        center = CANVAS_SIZE // 2
        if player:
            text = f'Winner: {player}'
        else:
            text = 'Draw'
        self.canvas.create_text(center, center, text=text, fill='white', font='Arial 50')
        self.canvas.unbind('<Button-1>')

        
    def click_event(self, event):
        print(event.x, event.y)
        self.event = event
        x_coord = event.x // FIGURE_SIZE
        y_coord = event.y // FIGURE_SIZE
        if x_coord == 3:
            x_coord = 2
        if y_coord == 3:
            y_coord = 2
        self.ind_x_coord = x_coord
        self.ind_y_coord = y_coord
        self.make_move(x_coord, y_coord)   
        if self.game_status:
            self.ai_best_move()    
    
    def make_move(self, x, y):
        d = {}
        for i in range(len(self.board)):
            d[i] = FIGURE_SIZE * i
        
        current_player = self.current_player

        if self.board[x][y] == EMPTY:
            self.update_board(x, y)
            self.change_player()
            if current_player == X:
                self.render_cross(d[x], d[y])
            elif current_player == O:
                self.render_circle(d[x], d[y])
        

    def update_board(self, x, y):
        c_player = self.current_player
        self.board[x][y] = c_player
        if self.check_win(self.board, c_player):
            self.winner(c_player)
            self.win_line(c_player)
        elif self.check_draw(self.board):
            self.winner()
    
    def win_line(self, c_player):
        x_win_line = 0
        y_win_line = 0
        if c_player == X:
            x_win_line = self.ind_x_coord
            y_win_line = self.ind_y_coord
        else:
            x_win_line = self.move[0]
            y_win_line = self.move[1]
            
        if self.coords == 1:
            self.canvas.create_line(0, (y_win_line * FIGURE_SIZE) + (FIGURE_SIZE // 2), CANVAS_SIZE, (y_win_line * FIGURE_SIZE) + (FIGURE_SIZE // 2), fill='green')
        if self.coords == 2:
            self.canvas.create_line((x_win_line * FIGURE_SIZE) + (FIGURE_SIZE // 2), 0, (x_win_line * FIGURE_SIZE) + (FIGURE_SIZE // 2), CANVAS_SIZE, fill='green')
        if self.coords == 3:
            self.canvas.create_line(0, 0, CANVAS_SIZE, CANVAS_SIZE, fill='green')
        if self.coords == 4:
            self.canvas.create_line(CANVAS_SIZE, 0, 0, CANVAS_SIZE, fill='green')
                
    def check_win(self, board, player):
        '''списки строятся вертикально'''
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
                self.coords = 2
                return True

        '''горизонтальная проверка'''
        for i in range(len(board)):
            if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                self.coords = 1
                return True
        
        '''проверка по диагонале справа-налево'''
        for i in range(3):
            if board[i][i] != player:
                False
            else:
                timer_left_right += 1
                if timer_left_right == 3:
                    self.coords = 3
                    return True

        '''проверка по диагонале слева-направо'''                     
        for i in range(3):
            if board[timer2[i]][timer[i]] != player:
                False
            else:
                timer_right_left += 1
                if timer_right_left == 3:
                    self.coords = 4
                    return True
                                  
    def check_draw(self, board):
        for row in board:
            if EMPTY in row:
                return False
        return True
    
    def change_player(self):
        if self.current_player == X:
            self.current_player = O
        else:
            self.current_player = X


    def minimax(self, board, isMax):
        board_len = range(len(self.board))

        if self.check_win(board, O):
            return 1
        elif self.check_win(board, X):
            return -1
        elif self.check_draw(board):
            return 0
        if isMax:
            best_score = float('-inf')
            for i in board_len:
                for j in board_len:
                    if board[i][j] == EMPTY:
                        board[i][j] = O
                        score = self.minimax(board, False)
                        board[i][j] = EMPTY
                        best_score = max(score, best_score)
        else:
            best_score = float('inf')
            for i in board_len:
                for j in board_len:
                    if board[i][j] == EMPTY:
                        board[i][j] = X
                        score = self.minimax(board, True)
                        board[i][j] = EMPTY
                        best_score = min(score, best_score)
        return best_score
    def ai_best_move(self):
        best_score = float('-inf')
        board_len = range(len(self.board))
        board = self.board[:]
        for i in board_len:
            for j in board_len:
                if board[i][j] == EMPTY:
                    board[i][j] = O
                    score = self.minimax(board, False)
                    board[i][j] = EMPTY
                    if score > best_score:
                        best_score = score
                        move = i, j
                        self.move = move
        
        self.make_move(move[0], move[1])


    


game_v1 = Board(start_player=FIRST_PLAYER)
game_v1.build_grid('red')
game_v1.mainloop()
