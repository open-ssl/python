'''
Write a function that finds the sum of the first n natural numbers.
Make your function recursive.
'''


def sum_numbers(num):
    return 1 if num == 1 else num + sum_numbers(num-1)


print(sum_numbers(5))
# sum_numbers(5) ➞ 15
# 1 + 2 + 3 + 4 + 5 = 15

# sum_numbers(1) ➞ 1

# sum_numbers(12) ➞ 78
