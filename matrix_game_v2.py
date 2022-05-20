from tkinter import *
from random import randint

CANVAS_SIZE = 600
PLAYER_SIZE = 20
X = 'player'
BLOCK_STEP = 'O'
matrix = []

class Board(Tk):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE)
        self.canvas.pack()
        matrix = []
        part = ['_'] * 30
        for i in range(30):
            matrix.append(part.copy())
        current_pos = [15, 15]
        self.x = current_pos[0]
        self.y = current_pos[1]
        matrix[self.y][self.x] = X
        self.matrix = matrix

    def main_player(self, color):
        ball = self.canvas.create_oval(self.y * PLAYER_SIZE, self.x * PLAYER_SIZE, self.y * PLAYER_SIZE + PLAYER_SIZE, self.x * PLAYER_SIZE + PLAYER_SIZE, fill=color)
        self.canvas.bind_all('<KeyPress>', self.move)
        self.ball = ball

    def move(self, event):
        if event.keysym == 'Up':
            if X in self.matrix[0]:
                pass
            elif self.matrix[self.y-1][self.x] == BLOCK_STEP:
                pass
            else:
                self.y -= 1
                self.matrix[self.y][self.x] = X
                self.matrix[self.y+1][self.x] = '_'
                self.canvas.move(self.ball, 0, -20)
        elif event.keysym == 'Down':
            if X in self.matrix[-1]:
                pass  
            elif self.matrix[self.y+1][self.x] == BLOCK_STEP:
                pass
            else:
                self.y += 1
                self.matrix[self.y][self.x] = X
                self.matrix[self.y-1][self.x] = '_'
                self.canvas.move(self.ball, 0, 20)               
        elif event.keysym == 'Left':
            if self.x == 0:
                pass 
            elif self.matrix[self.y][self.x - 1] == BLOCK_STEP:
                pass
            else:
                self.x -= 1
                self.matrix[self.y][self.x] = X
                self.matrix[self.y][self.x + 1] = '_'
                self.canvas.move(self.ball, -20, 0)
        elif event.keysym == 'Right':
            if self.x == 30 - 1:
                pass
            elif self.matrix[self.y][self.x + 1] == BLOCK_STEP:
                pass
            else:
                self.x += 1
                self.matrix[self.y][self.x] = X
                self.matrix[self.y][self.x - 1] = '_'
                self.canvas.move(self.ball, 20, 0)
                
    def block(self):
        y = -1
        for list_m in self.matrix:
            y += 1
            a = ''
            tr = True
            while tr:
                number_random = randint(0, 30//2+1)
                index_random = randint(0, 30-1)
                list_m[index_random] = BLOCK_STEP
                self.canvas.create_rectangle(index_random * PLAYER_SIZE, y * PLAYER_SIZE, index_random * PLAYER_SIZE + PLAYER_SIZE, y * PLAYER_SIZE + PLAYER_SIZE, fill='black')
                for i in list_m: 
                    if i == 'O':
                        a += i
                        if len(a) > number_random:
                            tr = False
          
    # """сетка"""
    # def markup(self):
    #     start_x = 0
    #     start_y = 0
    #     for i in range(30):
    #         start_x += 20
    #         start_y += 20
    #         self.canvas.create_line(start_x, 0, start_x, CANVAS_SIZE, fill='black')
    #         self.canvas.create_line(0, start_y, CANVAS_SIZE, start_y, fill='black')    
game_v1 = Board()
game_v1.main_player('red')
# game_v1.markup()
game_v1.block()
game_v1.mainloop()