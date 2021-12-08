limited_time = 3
while limited_time > 0:
    user_input = input()
    word = 'kr'
    for i in word:
        if i == user_input:
            print('good')
            break
    if i != user_input:     
        limited_time -= 1
        if limited_time == 0:
            print('вы проиграли')
        print(f'остлось {limited_time} попытки')
