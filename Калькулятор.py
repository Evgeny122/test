from distutils import command
from importlib.metadata import entry_points
from tkinter import *
# ф-ция, которая очищает поле
def clear():
    entry_field.delete(0, END)
# ф-ция, которая выполняет указанные вырожения
def answer():
    input_number = entry_field.get()
    summ = eval(input_number)
    entry_field.delete(0, END)
    entry_field.insert(999, summ)

root = Tk()
root.title('Simple Calculator 2000')
entry_field = Entry(root, width=40, borderwidth=5)
entry_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# кнопки(1-9)
button_1 = Button(root, text='1',command=lambda : entry_field.insert(999, 1), padx=40, pady=20)
button_2 = Button(root, text='2',command=lambda : entry_field.insert(999, 2), padx=40, pady=20)
button_3 = Button(root, text='3',command=lambda : entry_field.insert(999, 3), padx=40, pady=20)
button_4 = Button(root, text='4',command=lambda : entry_field.insert(999, 4), padx=40, pady=20)
button_5 = Button(root, text='5',command=lambda : entry_field.insert(999, 5), padx=40, pady=20)
button_6 = Button(root, text='6',command=lambda : entry_field.insert(999, 6), padx=40, pady=20)
button_7 = Button(root, text='7',command=lambda : entry_field.insert(999, 7), padx=40, pady=20)
button_8 = Button(root, text='8',command=lambda : entry_field.insert(999, 8), padx=40, pady=20)
button_9 = Button(root, text='9',command=lambda : entry_field.insert(999, 9), padx=40, pady=20)
button_0 = Button(root, text='0',command=lambda : entry_field.insert(999, 0), padx=40, pady=20)
# кнопки(+, -, X, //)
button_add = Button(root, text='+',command=lambda : entry_field.insert(999, '+'), padx=39, pady=20)
button_sub = Button(root, text='-',command=lambda : entry_field.insert(999, '-'), padx=39, pady=20)
button_mult = Button(root, text='x',command=lambda : entry_field.insert(999, '*'), padx=39, pady=20)
button_diff = Button(root, text='//',command=lambda : entry_field.insert(999, '//'), padx=39, pady=20)
# кнопки (Clear, =)
button_equa1 = Button(root, text='=',command=answer, padx=40, pady=20)
button_clear = Button(root, text='Clear',command=clear, padx=40, pady=20)

# кнопки (1, 9)
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)

# выражения + - * // 
button_add.grid(row=7, column=0)
button_sub.grid(row=7, column=1)
button_mult.grid(row=6, column=2)
button_diff.grid(row=6, column=1)

# очистка(clear) и равно(=)
button_equa1.grid(row=9, column=0)
button_clear.grid(row=8, column=0)

# сдвигаем кнопки Clear, = на 3 вправо
button_clear.grid(row=9, column=0, columnspan=3, sticky='we')
button_equa1.grid(row=8, column=0, columnspan=3, sticky='we')

root.mainloop()


