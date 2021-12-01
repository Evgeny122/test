a = 'or'
foo = '__'
list_foo = list(foo)
bar = ''
# нашли схожую букву
while a != foo:
    n = input()
    for baz in a:
        if baz == n:
# нашли индекс схожий буквы
                for index, i in enumerate(a):
                    if i == n:
                        list_foo[index] = n
                        foo = (''.join(list_foo))
                        print(foo)
        elif baz != n:
            print('нет')
                
# вставляем букву в foo
print('молодец')
