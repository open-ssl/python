# Text Type:
import random

str
print(str('stas'))

# Numeric Types:
int, float, complex
print(int('123'))
print(float('123.22211'))
print(type(float('123.22211')))
print(complex('1000'))
print(type(complex('1000')))

# Sequence Types:
list, tuple, range
print(list('New, hello, world, !'))
print(type(list('New, hello, world, !')))

print(tuple('stas'))
print(type(tuple('stas')))

print(range(1, 20))
# range by default from 0
for i in range(20):
    print(i)

# Mapping Type:
dict

print(dict(zip(['1', '2', '3'], ['stas', 'raz', 'hardbass'])))
print(type(dict(zip(['1', '2', '3'], ['stas', 'raz', 'hardbass']))))

# Set Types:
set, frozenset

print(set([1, 2, 3, 4, 1]))
print(type(set([1, 2, 3, 4, 1])))
print(dir(set))

print(set([1, 2, 3, 4, 1]) & set([1, 2, 3, 5, 11]))
print(set([1, 2, 3, 4, 1]) | set([1, 2, 3, 5, 11]))
print(set([1, 2, 3, 4, 1]) ^ set([1, 2, 3, 5, 11]))
print(frozenset([1, 2, 3, 4, 1]))

# Boolean Type:
bool
print(bool(123))
print(bool(None))
print(bool(0))
print(bool(not bool))
print(bool(False))


# Binary Types:
bytes, bytearray, memoryview


print(b"Hello"[0])


print("RANDOM NUMBER IS {}".format(random.randrange(1, 10)))
# print(random.randrange(1, 10))
