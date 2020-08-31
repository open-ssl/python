'''
Write a function that calculates the factorial of a number recursively.
'''


factorial = lambda n: 1 if n == 0 else n * factorial(n-1)


# factorial(5) ➞ 120

# factorial(3) ➞ 6

# factorial(1) ➞ 1

# factorial(0) ➞ 1
