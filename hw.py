number = [1, -1, 0, 14, -15, 3.15, -3.15]

def f(n):
    back_number = []
    for i in n:
        if i != 0:
            i = i - i - i
            back_number.append(i)
        elif i == 0:
            back_number.append(i)
    return back_number

def apply_to_each(l, f):
    l = f(l)
    return

apply_to_each(number, f)
print(number)