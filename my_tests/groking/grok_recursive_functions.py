# определяем базовый и рекурсивный случаи

def recursive_sum(arr):
    return 0 if len(arr) == 0 else arr[0] + recursive_sum(arr[1:])


print(recursive_sum([1, 2, 4, 7, 6, 5, 5, 5, 5]))



def recursive_elements_count(arr):
    return 0 if len(arr) == 0 else 1 + recursive_elements_count(arr[1:])


print(recursive_elements_count([1, 2, 4, 7, 6, 5, 5, 5, 5]))


def recursive_find_max_num_in_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] if arr[0] > recursive_find_max_num_in_array(arr[1:]) else recursive_find_max_num_in_array(arr[1:])


print(recursive_find_max_num_in_array([1,2,17,4,5]))


 Рекурсивный бинарный поиск
def recursive_binary_find(arr, num):
    if len(arr) == 1:
        # print(arr[0])
        return arr[0] == num
    else:
        return recursive_binary_find(arr[:(len(arr)//2)], num) if arr[(len(arr)//2)] > num else recursive_binary_find(arr[(len(arr)//2):], num)


print(recursive_binary_find([1,2,3,4,5,6,7,8,9], 4))
