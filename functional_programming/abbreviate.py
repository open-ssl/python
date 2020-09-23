'''
Create a function which takes a sentence and returns its abbreviation.
Get all of the words over or equal to n characters in length and return the
first letter of each, capitalised and overall returned as a single string.
'''


def abbreviate(txt, num=4):
    return ''.join(i[0].capitalize() for i in txt.split() if len(i) >= num)


print(abbreviate("do it yourself"))
 # "Y"

print(abbreviate("do it yourself", 2))
# "DIY"
# "do" and "it" are included because the second parameter specified that word lengths 2 are allowed.

abbreviate("attention AND deficit OR hyperactivity THE disorder")
# "ADHD"
# Words below the default 4 characters are not included in the abbreviation.

print(abbreviate("the acronym of long word lengths", 5))
# "AL"
# "acronym" and "lengths" have 5 or more characters.
