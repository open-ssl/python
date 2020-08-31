def reorder_digits(lst, direction):
    reverse = False if direction=='asc' else True
    new_lst = [sorted(str(i),reverse=reverse) for i in lst]
    return [int(''.join(item)) for item in new_lst]

print(reorder_digits([1, 2, 3, 4], "asc"))
# ➞ [155, 134, 89, 44, 112]
# reorder_digits([515, 341, 98, 44, 211], "desc") ➞ [551, 431, 98, 44, 211]
# reorder_digits([63251, 78221], "asc") ➞ [12356, 12278]
# reorder_digits([63251, 78221], "desc") ➞ [65321, 87221]
# reorder_digits([1, 2, 3, 4], "asc")  ➞ [1, 2, 3, 4]
# reorder_digits([1, 2, 3, 4], "desc") ➞ [1, 2, 3, 4]
