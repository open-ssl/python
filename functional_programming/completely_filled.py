'''
Create a function that checks if the box is completely filled with the asterisk symbol *
'''

#
from math import sqrt
def completely_filled(lst):
    lst = [item for stroke in lst for item in stroke]
    return True if len(lst) < 5 else lst.count('*') == (sqrt(len(lst)) - 2) ** 2


def completely_filled(lst):
    return ' '.join(lst)
print(completely_filled([
  "#####",
  "#***#",
  "#***#",
  "#***#",
  "#####"
]))


'''
completely_filled([
  "#####",
  "#***#",
  "#***#",
  "#***#",
  "#####"
])  True

completely_filled([
  "#####",
  "#* *#",
  "#***#",
  "#***#",
  "#####"
])  False

completely_filled([
  "###",
  "#*#",
  "###"
])  True

completely_filled([
  "##",
  "##"
])  True
'''
