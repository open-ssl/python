'''
Create a function that returns the amount of duplicate characters in a string.
It will be case sensitive and spaces are included. If there are no duplicates, return 0.
'''


def duplicates(txt):
    return sum([txt.count(i) - 1 for i in set(txt) if txt.count(i) > 1])

print(duplicates("Hello World!"))
