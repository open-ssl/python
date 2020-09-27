'''
Write a function that takes as input two different dictionaries
and filters the keys in each dictionary to only keep keys
that exist in both dictionaries.
Store your result as a list with two dictionaries.
'''


def intersection(dct1, dct2):
    dct3 = {}
    dct4 = {}
    for i in set(dct1.keys()) & set(dct2.keys()):
        dct3.update({i : dct1[i]})
        dct4.update({i : dct2[i]})
    return [dct3, dct4]


dict1 = {"a": 5, "b": 13, "c": 7}
dict2 = {"b": 5, "c": 8, "d": 91, "e": 99}
dict3 = {"a": 1, "b": 34}
dict4 = {"c": 9, "d": 8}

print(intersection(dict1, dict2))
 # [{"b": 13, "c": 7}, {"b": 5, "c": 8}]

intersection(dict1, dict4)
 # [{"c": 7}, {"c": 9}]

print(intersection(dict3, dict4))
 # [{}, {}]
