from random import randint
n = int(input('Количество клеток: '))
matrix = []
part = ['_'] * n
obj = 'O'

for i in range(n):
    matrix.append(part.copy())

for list_m in matrix:
    a = ''
    tr = True
    while tr:
        number_random = randint(0, n//2+1)
        index_random = randint(0, n-1)
        list_m[index_random] = obj
        for i in list_m:
            if i == 'O':
                a += i
                if len(a) > number_random:
                    tr = False

current_pos = [0, 0]
x = current_pos[0]
y = current_pos[1]
matrix[y][x] = 'x'
save_x = 0
save_y = 0
print('для того, чтобы передвигаться по полю используйте w - вверх, s - вниз, a - влево, d - вправо')
for i in matrix:
    print(i)

while True:
    matrix[y][x] = 'x'
    matrix[save_y][save_x] = '_'
    user_input = str(input('куда пойдешь? '))
    if user_input == 'd':
        if x == n - 1:
            print('стена')
        elif matrix[y][x+1] == obj:
            print('s')
        else:
            x += 1
            matrix[y][x] = 'x'
            matrix[y][x - 1] = '_'
            for i in matrix:
                print(i)
        print('____________________')
        continue
        
            
    if user_input == 'a':
        if x == 0:
            print('там стена!')
        elif matrix[y][x-1] == obj:
            print('s')
        else:   
            x -= 1
            matrix[y][x] = 'x'
            matrix[y][x + 1] = '_'
            for i in matrix:
                print(i)
            print('____________________')
            continue
    if user_input == 'w':
        if 'x' in matrix[0]:
            print('там стена!')
        elif matrix[y-1][x] == obj:
            print('s') 
        else:      
           y -= 1
           matrix[y][x] = 'x'
           matrix[y + 1][x] = '_'
           for i in matrix:
               print(i)
        print('____________________')
        continue
        
    if user_input == 's':
        if 'x' in matrix[-1]:
            print('там стена!')
        elif matrix[y+1][x] == obj:
            print('s')
        else:            
           y += 1
           matrix[y][x] = 'x'
           matrix[y - 1][x] = '_'
           for i in matrix:
               print(i)
        print('____________________')
        continue
    if user_input == 'save':
        save_x = x
        save_y = y
        f = open('new_file' , 'w+')
        print('Game saved')
        for i in matrix:
           print(i)
           f.write(f'{str(i)}\n')                  
        f.close()
        print('Game saved')
        print('__________')
        continue

    if user_input == 'down':
        matrix[y][x] = '_'
        y = save_y
        x = save_x
        matrix[y][x] = 'x'
        for i in matrix:
            print(i)       
        print('Game loaded')
        print('___________')
        loaded_file = open('new_file', 'r')
        loaded_data = loaded_file.read()