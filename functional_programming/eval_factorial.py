'''
Create a function that takes a list of factorial expressions and returns the sum.
'''

import math
def eval_factorial(lst):
    return sum(math.factorial(int(i.split('!')[0])) for i in lst)

# print('2!'.split('!'))
# print(eval_factorial(["2!", "3!"]))


# eval_factorial(["2!", "3!"]) ➞ 8

# eval_factorial(["5!", "4!", "2!"]) ➞ 146

# eval_factorial(["0!", "1!"]) ➞ 2
