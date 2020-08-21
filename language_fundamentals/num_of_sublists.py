
'''
Return the total number of lists inside a given list.
'''


def num_of_sublists(lst):
    return len([i for i in lst if type(i) is list])


print(num_of_sublists([1, 2, 3]))

# num_of_sublists([[1, 2, 3]]) ➞ 1
# num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) ➞ 3
# num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]) ➞ 4
# num_of_sublists([1, 2, 3]) ➞ 0
