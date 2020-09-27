'''
Write a function that takes an integer n, reverses the binary representation
of that integer, and returns the new integer from the reversed binary.
'''

def reversed_binary_integer(num):
    return int('0b' + bin(num)[2:][::-1], 2)
# reversed_binary_integer(10)  5
# 10 = 1010 -> 0101 = 5

print(reversed_binary_integer(12))
# 12 = 1100 -> 0011 = 3

print(reversed_binary_integer(25))
 # 19
# 25 = 11001 -> 10011 = 19

# reversed_binary_integer(45)  45
# 45 = 101101 -> 101101 = 45

# print(bin(3)[2:])
