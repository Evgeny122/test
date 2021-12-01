answer = 'or'
closed = '__'
list_closed = list(closed)
# нашли схожую букву
while answer != closed:
    user_input = input()
    for n in answer:
        if n == user_input:
# нашли индекс схожей буквы
                for index, i in enumerate(answer):
                    if i == user_input:
                        list_closed[index] = user_input
                        closed = (''.join(list_closed))
                        print(closed)
# не могу сделать так, что когда мы пишем не верную букву, он нам писал 'нет'
# у меня получается так, что он в любом случае пишет 'нет', так как цикл на 8 строчке переберает дальше буквы, даже после того как нашел нужную
#  ??????? как мне остановить этот чертов цикл?)
        elif n != user_input:
            print('нет')
                
# вставляем букву в closed
print('молодец')
