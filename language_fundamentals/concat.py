'''
Create a function that concatenates n input lists, where n is variable.
'''


def concat(*args):
    return [i for item in args for i in item]


print(concat([1, 2, 3], [4, 5], [6, 7]))

# concat([1, 2, 3], [4, 5], [6, 7]) ➞ [1, 2, 3, 4, 5, 6, 7]
# concat([1], [2], [3], [4], [5], [6], [7]) ➞ [1, 2, 3, 4, 5, 6, 7]
# concat([1, 2], [3, 4]) ➞ [1, 2, 3, 4]
# concat([4, 4, 4, 4, 4]) ➞ [4, 4, 4, 4, 4]
