'''Write a function that takes in a string s and returns a function that returns s.'''


def redundant(txt):
	return lambda: print(txt)

f1 = redundant('stas')
f1()


# f1 = redundant("apple")
# f1() ➞ "apple"

# f2 = redundant("pear")
# f2() ➞ "pear"

# f3 = redundant("")
# f3() ➞
