'''
Write a function that transforms a list of characters into a list of dictionaries, where:

The keys are the characters themselves.
The values are the ASCII codes of those characters.
'''


def to_dict(lst):
	return list(map(lambda x: {x: ord(x)}, lst))



print(to_dict(['a', 'b', 'c']))


# to_dict(["a", "b", "c"]) ➞ [{"a": 97}, {"b": 98}, {"c": 99}]
# to_dict(["^"]) ➞ [{"^": 94}]
# to_dict([]) ➞ []
