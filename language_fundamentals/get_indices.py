'''
Create a function that returns the indices of all occurrences of an item in the list.
'''

def get_indices(lst, el):
    return [i for i, b in enumerate(lst)]

def get_indices_2(lst, el):
    return [i for i in range(len(lst))]

print(get_indices([1, 5, 5, 2, 7], '1'))



# get_indices(["a", "a", "b", "a", "b", "a"], "a") ➞ [0, 1, 3, 5]
# get_indices([1, 5, 5, 2, 7], 7) ➞ [4]
# get_indices([1, 5, 5, 2, 7], 5) ➞ [1, 2]
# get_indices([1, 5, 5, 2, 7], 8) ➞ []
