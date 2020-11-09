from math import sqrt
def quadratic_equation(arg1, arg2, arg3):
    discr = int(sqrt(arg2 ** 2 - 4 * arg1 * arg3))
    return sorted([(-arg2 - discr),(-arg2 + discr)])[1] // (2 * arg1)
print(quadratic_equation(1, 2, -3))
 # ➞ 1

print(quadratic_equation(2, -7, 3))
 # ➞ 3

print(quadratic_equation(1, -12, -28))
 # ➞ 14
