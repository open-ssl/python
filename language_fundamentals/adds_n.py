'''
Write a function that returns a lambda expression, which adds n to its input
'''


def adds_n(n):
	return lambda x : x + n



adds1 = adds_n(1)
adds10 = adds_n(10)
adds5neg = adds_n(-5)
adds0 = adds_n(0)


# print(adds1(3))
# print(adds1(10))
# print(adds10(30))
# print(adds10(50))
# print(adds5neg(0))
# print(adds5neg(6))
# print(adds0(7))
# print(adds0(66))
