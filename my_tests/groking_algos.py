# Binary Search
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

# Sort by choise
def find_smallest(arr):
    smallest = arr[0]
    index = len(arr)
    for i in range(1, index):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

def selection_sort(arr):
    new_arr = []
    while arr:
        smallest = find_smallest(arr)
        new_arr.append(smallest)
        arr.pop(arr.index(smallest))
    return new_arr

print(selection_sort([1,2,4,5,-60,777,0, 100]))
