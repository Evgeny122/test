f = '"Ура!", вопите, дети, повару'
w = ''
for i in f.lower():
    if i in 'йцукенгшщзхъфывапролджэёячсмитьбю':
        w += i
def palindrome(string):
    b = True
    while b: 
        if string[0] == string[-1]:
            string = string.replace(string[0], '')
            string = string.replace(string[-1], '')
        if len(string) == 1:
            b = False
            return print('is a palindrome')
        elif string[0] != string[-1]: 
            print('is not a palindrome')
            b = False
palindrome(w)
    


    
