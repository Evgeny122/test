'''1 задание'''
def domain_name(url):
    return url.split('//')[-1].split('www.')[-1].split('.')[0]


'''2 задание'''
from ipaddress import IPv4Address
def int32_to_ip(int32):
    ip_addr = IPv4Address(int32)
    return str(ip_addr)


'''3 задание'''
def zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count
 


'''4 задание'''
import itertools
def bananas(string):
    result = set()
    
    for combm in itertools.combinations(range(len(string)), len(string) - 6):
        arr = list(string)
        
        for i in combm:
            arr[i] = '-'
        
        candidate = ''.join(arr)
        
        if candidate.replace('-', '') == 'banana':
            result.add(candidate)
    
    return result


'''5 задание'''
from functools import reduce
import itertools
def count_find_num(numbers, limited):

    base_case = reduce(lambda a, b: a * b, numbers)
    if base_case > limited:
        return []
    
    test_vol = base_case
    a = True
    min_vol = min(numbers)
    count = 0

    while a:
        test_vol *= min_vol

        if test_vol <= limited:
            count += 1
        else:
            repeat_limited = count + len(numbers)
            a = False

    
    lst_summ = [base_case]            

    while repeat_limited != len(numbers):
        code_vars = itertools.combinations_with_replacement(numbers, repeat_limited)
        for var in code_vars:
            ans_var = 1
            if len(set(var)) == len(numbers):
                for i in var:
                    ans_var *= i
                if ans_var <= limited:
                    lst_summ.append(ans_var)
        repeat_limited -= 1
    return [len(lst_summ), max(lst_summ)]

                








