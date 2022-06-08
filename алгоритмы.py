'''бинарный поиск'''
# from random import randint


# def tr(data, target):
#     if data == []:
#         return False
#     elif len(data) == 1:
#         return data[0] == target
#     else:
#         half = len(data) // 2
#         if data[half] > target:
#             return tr(data[:half], target)
#         else:
#             return tr(data[half:], target)
# ls = [1, 2, 4, 5, 8, 10, 15, 20, 30, 31, 43]
# tr(ls, 31)

'''алгоритм сортировки'''
# foo = [75, 26, 45, 74, 63, 85, 65, 43, 59, 64]
# new = []
# def sort(a):
#     while len(a) > 0:
#         f = a[0]
#         dev = range(0, len(a))
#         ind = 0

#         for i in dev:
#             if a[i] < f:
#                 f = a[i]
#                 ind = i
#         a.pop(ind)
#         new.append(f)
#     return new
# sort(foo)

"""алгоритм сортировки"""

# foo = [1,3,5,2,4]
# def quick_sort(arr, low, high):
#     if low < high:
#         pivot = partition(arr, low, high)
#         quick_sort(arr, low, pivot - 1)
#         quick_sort(arr, pivot + 1, high)

# def partition(arr, low, high):
#     i = (low - 1)
#     pivot = arr[high]

#     for j in range(low, high):
#         if arr[j] < pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i] 
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return i + 1
# quick_sort(foo, 0, 4)
# print(foo)
'''алгоритм дейкстры'''
# def find_lowest_cost_node(costs):
#     lowest_cost = float("inf")
#     lowest_cost_node = None

#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node

# """узлы"""
# graph = {'start': {'a': 6, 'b': 2}, 'a': {'finish': 1}, 'b': {'a': 3, 'finish': 5}, 'finish': {}}
# """бесконечность"""
# infinity = float("inf")
# """стоимость"""
# costs = {'a': 6, 'b' : 2, 'finish': infinity}
# """родители"""
# parents = {'a': 'start', 'b': 'start', 'finish': None }
# """массимв для отслеживания отрабтаных узлов """
# processed = []
# node = find_lowest_cost_node(costs)
# lst = []

# while node is not None:
#     cost = costs[node]
#     neighbors = graph[node]

#     for n in neighbors.keys():
#         new_cost = cost + neighbors[n]
#         if costs[n] > new_cost:
#             costs[n] = new_cost
#             parents[n] = node

#     processed.append(node)
#     node = find_lowest_cost_node(costs)

# print(parents)
# point = 'finish'
# while point != 'start':
#     point = parents[point]
#     lst.append(point)
# lst.insert(0, 'finish')
# lst.reverse()
# print(lst)
# print(parents[parents[parents['finish']]])
# l = [1, 3, 4 , 5]






# an = 0
# for i in l:
#     an += i
# print(an)

# def rec(a): 
#     if a == []:
#         return 0
#     else:
#         return 1 + rec(a[1:]) 
# print(rec(l))

'''связанные списки(Linked_list)'''
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#     def append(self, val):
#         end = Node(val)
#         n = self
#         while (n.next):
#             n = n.next
#         n.next = end
# ll = Node(1)
# ll.append(2)
# ll.append(3)
# node = ll
# print(node.data)
# while node.next:
#     node = node.next
#     print(node.data)
'''создание массива'''
# import array as arr

'''название массива = указать какие элементы хранятся в массиве[элементы массива]'''
#variable_name = array(typecode, [elements])

# numbers = arr.array('i', [10, 20, 30])

# print(numbers)
# print(len(numbers))
# print(numbers[2])
'''рекурсия'''

# def chek(st, lt):
#     if not st:
#         return 0
#     elif st[0] == lt:
#         return 1 + chek(st[1:], lt)
#     else:
#         return chek(st[1:], lt)
# string = 'gtgy'
# letter = 'g'
# print(chek(string, letter))

def sum(mas):
    if len(mas) <= 0:
        return 0
    else:
        return mas[0] + sum(mas[1:])

lst = [1, 3, 5, 6]
print(sum(lst))

        

def lenn(mas):
    if len(mas) == 0:
        return 0
    else:
        return 1 + lenn(mas[1:])

print(lenn(lst))

