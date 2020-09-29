'''
Create a function that returns the subarrays of n consecutive
elements from the original element that sum up to k.
The function will have the following form: sliding_sum(lst, n, k)
'''
def sliding_sum(lst, num1, num2):
    return_lst = []
    for i in range(len(lst)):
        tmp = []
        for j in range(i, len(lst)):
            if sum(tmp) + lst[j] <= num2:
                tmp.append(lst[j])
                if sum(tmp) == num2 and len(tmp) == num1:
                    return_lst.append(tmp)
            else:
                break
    return return_lst

print(sliding_sum([1, 4, 2, 3, 5, 0], 2, 5))

# sliding_sum([1, 4, 2, 3, 5, 0], 2, 5) ➞ [[1, 4], [2, 3], [5, 0]]

print(sliding_sum([5, 5, 5, 5, 5], 1, 5))
# [[5], [5], [5], [5], [5]]

print(sliding_sum([5, 5, 5, 5, 5], 5, 24))
