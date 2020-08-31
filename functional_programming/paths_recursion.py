'''
Given a list of cities and the distances between each pair of cities,
what is the shortest possible route that visits each city and returns to the origin city?

Return the total number of possible paths a salesman can travel, given n paths.
'''


def paths(n):
	return 1 if n == 1 else n * paths(n-1)


paths = lambda n: 1 if n == 1 else n * paths(n-1)
# paths(4) ➞ 24

# paths(1) ➞ 1

# paths(9) ➞ 362880
