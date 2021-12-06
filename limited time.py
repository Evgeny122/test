limited_time = 3
user_input = '3'
word = 'f'
for i in word:
    if i == user_input:
        print('good')
for i in word:
    if i != user_input:    
        # для всех букв в слове сравниваешь с вводом -  слово: кот, ввод: о, к != о, о == о, т != о. Получится 2 ошибки.
        limited_time -= 1
        if limited_time == 0:
            print('вы проиграли')
            break
        print(f'остлось {limited_time} попытки')
        break
