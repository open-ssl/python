'''
Write a function that sorts the positive numbers in ascending order,
and keeps the negative numbers untouched.
'''

def pos_neg_sort(lst):
    lst2 = sorted([i for i in lst if i > 0])
    dct = dict(zip([i for i in lst if i > 0], [lst.index(i) for i in lst if i > 0]))
    i = 0
    for it in lst:
        if it > 0:
            lst[dct[it]] = lst2[i]
            i +=1
    return lst


# print(pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]))

# pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) ➞ [2, 3, -2, 5, -8, 6, -2]
#
# pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]) ➞ [1, 2, 3, -1, 4, 5, -1, 6]
#
# pos_neg_sort([-5, -5, -5, -5, 7, -5]) ➞ [-5, -5, -5, -5, 7, -5]
#
# pos_neg_sort([]) ➞ []
