# Return the coordinates ([row, col]) of the element that differs from the rest.


def where_is_waldo(lst):
    clear_lst = [i for item in lst for i in item]
    item =  [i for i in set(clear_lst) if clear_lst.count(i) == 1][0]
    for i, it in enumerate(lst):
        if item in it:
            return [i+1, it.index(item)+1]


'''
print(where_is_waldo([
  ["A", "A", "A"],
  ["A", "A", "A"],
  ["A", "B", "A"]
]))

print(where_is_waldo([
  ['A']
]))

where_is_waldo([
  ["A", "A", "A"],
  ["A", "A", "A"],
  ["A", "B", "A"]
]) ➞ [3, 2]

where_is_waldo([
  ["c", "c", "c", "c"],
  ["c", "c", "c", "d"]
]) ➞ [2, 4]

where_is_waldo([
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["P", "O", "O", "O"],
  ["O", "O", "O", "O"]
]) ➞ [5, 1]
'''
