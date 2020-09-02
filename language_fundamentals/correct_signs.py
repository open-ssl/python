'''
Create a function that returns true if a given
inequality expression is correct and false otherwise.
'''

import re

# correct_signs("3 < 7 < 11") ➞ True
# correct_signs("13 > 44 > 33 > 1") ➞ False
# correct_signs("1 < 2 < 6 < 9 > 3") ➞ True

def correct_signs(text):
    lst1 = re.findall('\d+', text)
    lst2 = re.findall('>|<', text)
    count = 1
    for item, item1 in zip(lst2, lst1):
        if not eval('{}{}{}'.format(item1,item,lst1[count])):
            return False
        count +=1
    return True

print(correct_signs("1 < 2 < 6 < 9 > 3"))
# print(eval("2 < 3"))
