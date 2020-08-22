'''
Write a function that converts a dictionary into a list, where each element represents a key-value pair.
'''

def to_list(dct):
    return sorted([[i1, i2] for i1, i2 in zip(dct.keys(), dct.values())])


def to_list2(d):
    return sorted(list(i) for i in d.items())


print(to_list({ 'foo': 33, 'bar': 45, 'baz': 67 }))
print(to_list2({ 'foo': 33, 'bar': 45, 'baz': 67 }))


# to_list({ "a": 1, "b": 2 }) ➞ [["a", 1], ["b", 2]]
# to_list({ "shrimp": 15, "tots": 12 }) ➞ [["shrimp", 15], ["tots", 12]]
# to_list({}) ➞ []
