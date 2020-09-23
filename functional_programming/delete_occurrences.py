'''
Create a function that takes two arguments:
a list and a number. In the list (the first argument),
if an element occurs more than N times (the second argument),
remove the extra occurrence(s) and return the result.
'''


def delete_occurrences(lst, num):
    return [j for i, j in enumerate(lst) if lst[:i].count(j) < num]

# print(delete_occurrences([1, 1, 1, 1], 2))

print(delete_occurrences([13, True, 13, None], 1))
# [13, True, None]

# delete_occurrences([True, True, True], 3)  [True, True, True]
