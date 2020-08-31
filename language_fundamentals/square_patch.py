'''
Create a function that takes an integer and outputs
an n x n square solely consisting of the integer n.
'''


def square_patch(n):
    lst = []
    for i in range(n):
        lst.append([n] * n)
    return lst


def square_patch2(n):
    return [[n]*n]*n


'''
square_patch(3) ➞ [
  [3, 3, 3],
  [3, 3, 3],
  [3, 3, 3]
]

square_patch(5) ➞ [
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5]
]

square_patch(1) ➞ [
  [1]
]

square_patch(0) ➞ []
'''
