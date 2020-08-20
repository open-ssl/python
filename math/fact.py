from math import sqrt

def quadratic_equation(a, b, c):
    d = sqrt(b ** 2 - 4 * a * c)
    r1 = -b + int(d) // (2 * a)
    r2 =  -b -  int(sqrt(d)) // (2 * a)
    return (r1, r2, d)
    return int(r1) if int(r1) - r1 == 0 else int(r2)


print(quadratic_equation(1, 2, -3))
