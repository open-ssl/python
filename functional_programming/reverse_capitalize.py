'''
Create a function that takes a string of lowercase characters and returns that string reversed and in upper case.
'''

def reverse_capitalize(txt):
	return txt[::-1].upper()


print(reverse_capitalize('abc'))


# reverse_capitalize("abc") ➞ "CBA"

# reverse_capitalize("hellothere") ➞ "EREHTOLLEH"

# reverse_capitalize("input") ➞ "TUPNI"
