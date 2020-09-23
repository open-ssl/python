'''
Write a function that takes a string, and returns a new string with any duplicate consecutive letters removed.
'''


def unstretch(txt):
    return txt[0] + ''.join([txt[i] for i in range(1, len(txt)) if txt[i-1] != txt[i]])
    # return

print(unstretch("ppoeemm"))
# ➞ "poem"

print(unstretch("wiiiinnnnd"))
 # ➞ "wind"

unstretch("ttiiitllleeee")
 # ➞ "title"

print(unstretch("cccccaaarrrbbonnnnn"))
# ➞ "carbon"
