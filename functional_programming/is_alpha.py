'''
Create a function that takes a string and returns True if the sum of
the position of every letter in the alphabet is even and False if the sum is odd.
'''

# def is_alpha(txt):
    return not sum([ord(i) - 96 for i in txt.lower() if 96 < ord(i) < 123]) % 2
# print(ord('z') - 96)
# chr()
# print(is_alpha('True'))
# print(is_alpha("i'am king"))
# 9 + 1 + 13 + 11 + 9 + 14 + 7 = 64 (even)

# is_alpha("True")
# 20 + 18 + 21 + 5= 64 (even)

# print(is_alpha("alexa"))
# 1 + 12 + 5 + 24 + 1= 43 (odd)

print('l'.isalpha())
