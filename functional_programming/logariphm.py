from math import log
def logarithm(n1, total):
	logic = n1 > 1 and total > 1 and log(total, n1)
    return int(log(total, n1)) if logic else 'Invalid'

# print(logarithm(1, len("Hi,")))
# ➞ 2
#
# print(1)
# print(logarithm(2, 64))
# print(logarithm(7, 49))

# print(logarithm(4, 64))
# print(logarithm(5, 9765625))


#  # ➞ 6
#
# # print(logarithm(2, 4))
#  # ➞ 2




import math

# print(int(math.log(16, 2)))



print([1, 20] > 2)
