'''
Given a number, create a function that returns a new number based on these rules:

For each digit, replace it by the number of times it appears in the number.
The final instance of the number will be an integer, not as a string.

digit_count(136116) ➞ 312332
# The number 1 appears thrice, so replace all 1s with 3s.
# The number 3 appears only once, so replace all 3s with 1s.
# The number 6 appears twice, so replace all 6s with 2s.
# Return as an integer.
'''


def digit_count(num):
    num = str(num)
    return ''.join([str(num.count(i)) for i in num])
    # return ''.join([str(num).count(str(i)) for i in str(num)])
print(digit_count(221333))
# 221333


print(digit_count(136116))
# 312332

# digit_count(2)  1
