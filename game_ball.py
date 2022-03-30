from tkinter import *
from time import sleep

root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()

class Circle:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.size = 50
        self.speed_x = 3
        self.speed_y = 2
        self.object = canvas.create_oval(self.x, self.y, self.size, self.size, fill='red')
        self.canvas_size = 600
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        canvas.move(self.object, self.speed_x, self.speed_y)
        self.check_collision()

    def check_collision(self):
        pos = canvas.coords(self.object)
        if pos[0] <= 0:
            self.speed_x *= -1
        if pos[2] >= self.canvas_size:
           self.speed_x *= -1
        if pos[1] <= 0:
            self.speed_y *= -1
        if pos[3] >= self.canvas_size:
            self.speed_y *= -1
class Wall:
    def __init__(self):
        self.sq_x1 = 245
        self.sq_y1 = 470
        self.sq_x2 = 355
        self.sq_y2 = 490
        self.obj = canvas.create_rectangle(self.sq_x1, self.sq_y1, self.sq_x2, self.sq_y2, fill='green')
        self.obj = canvas.bind_all('<KeyPress>', self.left_right)
    
    def left_right(self, event):
        if event.keysym == 'Left':
            canvas.move(self.obj, -50, 0)
        elif event.keysym == 'Right':
            canvas.move(self.obj, 50, 0)

    
c1 = Circle()
c2 = Wall()
while True:
    c1.move()
    root.update()
    sleep(0.005)

root.mainloop()