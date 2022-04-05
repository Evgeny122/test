
from random import randint

n = 9
matrix = []
part = ['_'] * 9
for i in range(n):
    matrix.append(part.copy())


one_square = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
two_square = [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]]
three_square = [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2, 7], [2, 8]]
four_square = [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]]
five_square = [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]]
six_square = [[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8]]
seven_square = [[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8, 1], [8, 2]]
eight_square = [[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 0], [8, 1], [8, 2]]
nine_square = [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]] 


lst_square = [one_square, two_square, three_square, four_square, five_square, six_square, seven_square, eight_square, nine_square]

random_number_in_matrix = 40
number_in_matrix = 0
while number_in_matrix != random_number_in_matrix:
    strig_m = randint(0, 9)
    column = randint(0, 9)
    coords = [strig_m, column]
    random_number = randint(1, 9)
    lst_sq = []
    list_y = []
    for sq in lst_square:
        if coords in sq:
            for i in sq:
                lst_sq.append(matrix[i[0]][i[1]])
            for i in matrix:
                    list_y.append(i[column])
            if str(random_number) not in lst_sq and str(random_number) not in matrix[strig_m] and  str(random_number) not in list_y:
                matrix[strig_m][column] = str(random_number)
                number_in_matrix += 1
            
        continue
    continue   
for i in matrix:
    print(i)

while True:
    list_user = []
    list_one_square = []
    list_two_square = []
    list_four_square = []

    b = True
    # пользователь вводит число
    user = input('???????  ')
    for i in user:
        list_user.append(int(i))
    
    # определил квадрат
    # ПЕРВЫЙ КВАДРАТ
    if list_user[0:-1] in one_square:
        list_xy = []
        # добавляет в список все значения, которые есть в данном квадрате 
        for i in one_square:
            list_one_square.append(matrix[i[0]][i[1]])
            # проверка, есть ли значение, которое ввел юзер в нашем квадрате
            for i in list_one_square:
                if i == str(list_user[2]):
                    b = False
                if b == True:
                    for i in matrix[list_user[0]]:
                        if i == str(list_user[2]):
                            b = False
                if b == True:
                    list_xy = []
                    for i in matrix:
                        list_xy.append(i[list_user[1]])
                        for n in list_xy:
                            if n == str(list_user[2]):
                                b = False

                
        # если значния нет, значит мы его добавляем в квадрат 
        if b == True:
            matrix[list_user[0]][list_user[1]] = str(list_user[2])

    # __________________________________________________________________________

    # ВТОРОЙ КВАДРАТ
    if list_user[0:-1] in two_square:
        # добавляет в список все значения, которые есть в данном квадрате 
        for i in two_square:
            list_two_square.append(matrix[i[0]][i[1]])
            # проверка, есть ли значение, которое ввел юзер в нашем квадрате
            for i in list_two_square:
                if i == str(list_user[2]):
                    b = False
                if b == True:
                    for i in matrix[list_user[0]]:
                        if i == str(list_user[2]):
                            b = False
                if b == True:
                    list_xy = []
                    for i in matrix:
                        list_xy.append(i[list_user[1]])
                        for n in list_xy:
                            if n == str(list_user[2]):
                                b = False
        
                
        # если значния нет, значит мы его добавляем в квадрат 
        if b == True:
            matrix[list_user[0]][list_user[1]] = str(list_user[2])
    # __________________________________________________________________________

    if list_user[0:-1] in four_square:
        # добавляет в список все значения, которые есть в данном квадрате 
        for i in four_square:
            list_four_square.append(matrix[i[0]][i[1]])
            # проверка, есть ли значение, которое ввел юзер в нашем квадрате
            for i in list_four_square:
                if i == str(list_user[2]):
                    b = False
                if b == True:
                    for i in matrix[list_user[0]]:
                        if i == str(list_user[2]):
                            b = False
                if b == True:
                    list_xy = []
                    for i in matrix:
                        list_xy.append(i[list_user[1]])
                        for n in list_xy:
                            if n == str(list_user[2]):
                                b = False
        
                
        # если значния нет, значит мы его добавляем в квадрат 
        if b == True:
            matrix[list_user[0]][list_user[1]] = str(list_user[2])
    # __________________________________________________________________________

    # print(list_square)
    # print(list_xy)
    print('_____________')
    for i in matrix:
        print(i)