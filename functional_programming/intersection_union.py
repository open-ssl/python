'''
Create a function that returns the characters from a list or string r on odd
or even positions, depending on the specifier s. The specifier will be "odd" for items
on odd positions (1, 3, 5, ...)
and "even" for items on even positions (2, 4, 6, ...).
'''


def char_at_pos(r, s):
    stroke = [r[i] for i in range(1 if s == 'even' else 0, len(r), 2)]
    return stroke if isinstance(r, list) else ''.join(stroke)



print(char_at_pos([2, 4, 6, 8, 10], "even"))


# char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 2nd & 4th positions

# print(char_at_pos("EDABIT", "odd"))
 # ➞ "EAI"
# "E", "A" and "I" occupy the 1st, 3rd and 5th positions

# char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd") ➞ ["A", "B", "T", "A", "I", "Y"]
