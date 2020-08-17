import re
import unittest

'''
Write a function that splits a string into substrings of size n,
adding a specified delimiter between each of the pieces.
'''

def split_and_delimit1(txt, num, delimiter):
    return_value = f'{delimiter}'.join(i for i in re.findall('.'*num,txt))
    value = len(txt) % num
    if value != 0:
        return_value += delimiter + txt[len(txt) - value:]
    return return_value

def split_and_delimit2(txt, num, delimiter):
    return delimiter.join(txt[i: i + num] for i in range(0, len(txt), num))

print(split_and_delimit1("bellow", 2, "&"))
print(split_and_delimit1("magnify", 3, ":"))
print(split_and_delimit1("poisonous", 2, "~"))
print(split_and_delimit1("shape-shifting", 5, '^'))

print(split_and_delimit2("bellow", 2, "&"))
print(split_and_delimit2("magnify", 3, ":"))
print(split_and_delimit2("poisonous", 2, "~"))
print(split_and_delimit2("shape-shifting", 5, '^'))

# split_and_delimit("bellow", 2, "&") ➞ "be&ll&ow"
# split_and_delimit("magnify", 3, ":") ➞ "mag:nif:y"
# split_and_delimit("poisonous", 2, "~") ➞ "po~is~on~ou~s"
