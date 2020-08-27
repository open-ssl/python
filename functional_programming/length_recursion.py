'''
Write a function that returns the length of a string. Make your function recursive.
'''


def length(txt):
	return (0 if txt == '' else 1 + length(txt[:-1]))


# length("apple") ➞ 5
#
# length("make") ➞ 4
#
# length("a") ➞ 1
#
# length("") ➞ 0
