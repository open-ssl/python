# Binary Search
# ''Время выполнения log n

def b_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        num = (high + low) // 2

        if lst[num] == item:
            return num
        if lst[num] < item:
            low = num + 1
            continue
        high = num - 1

print(b_search([1, 2, 3, 4, 5], 6))



# Простой поиск
# n


# Быстрая сортировка
# Работает быстрее сортировки выбором
# n log n

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        key_item = arr[0]
        lst1 = [i for i in arr if i < key_item]
        lst2 = [i for i in arr if i > key_item]
        return quick_sort(lst1) + [key_item] + quick_sort(lst2)


print(quick_sort([55,2,3,22,8, 777]))



# Сортировка выбором
# Время работы n^2    на самом деле около 1/2 * n * n
#
#
def sort_by_choise_func(arr):
    return_arr = []
    while len(arr):
        max_item = arr[0]
        for item in arr:
            if item > max_item:
                max_item = item
        return_arr.append(arr.pop(arr.index(max_item)))
    return return_arr

print(sort_by_choise_func([1,222,4,10,13]))



# задача о комивояжере
# n!


# алгоритм поиска в глубину BFT основан на использовании очереди
# и графа
from collections import deque

graph = {}
graph['you'] = ["alice", "bob", "claire"]
graph['alice'] = ["peggy"]
graph['bob'] = ["anuj", "peggy"]
graph['claire'] = ["claire", "thom", "jonny"]
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

#  создал очередь
search_deque = deque()
search_deque += graph['you']
checked_names_list = []

def search(search_deque):
    while search_deque:
        # последовательно удаляем из очереди первых пришедших в неё участников
        person = search_deque.popleft()
        if person not in checked_names_list:
            if is_mango_seller(person):
                print(f'We found him! IT IS {person}')
                print(checked_names_list)
                return True
            else:
                search_deque += graph[person]
                checked_names_list.append(person)
    return False

def is_mango_seller(name):

    return name[-1] == 'm'

search(search_deque)
