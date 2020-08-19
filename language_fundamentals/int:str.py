'''
Python got drunk and the built-in functions str() and int() are acting odd:

str(4) ➞ 4

str("4") ➞ 4

int("4") ➞ "4"

int(4) ➞ "4"
You need to create two functions to substitute str() and int().
A function called int_to_str() that converts integers into strings and a function
alled str_to_int() that converts strings into integers.
'''


str, int = int, str
def int_to_str(num):
    return str(num)


def str_to_int(num):
	return int(num)


print(int_to_str(4))
print(str_to_int('4'))
