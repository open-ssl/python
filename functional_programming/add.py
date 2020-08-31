'''
Given a number, n, return a function which adds n to the number passed to it.
'''


def add(n):
    return lambda x: n+x


print(add(10)(20))

# add(10)(20) ➞ 30

# add(0)(20) ➞ 20

# add(-30)(80) ➞ 50
