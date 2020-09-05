'''
Create a function that takes a string and censors words over four characters with *.
'''

def censor(txt):
    return ' '.join([i if len(i) <5 else len(i) * '*' for i in txt.split(' ')])

'''
censor("The code is fourty") ➞ "The code is ******"

censor("Two plus three is five") ➞ "Two plus ***** is five"

censor("aaaa aaaaa 1234 12345") ➞ "aaaa ***** 1234 *****"
'''

print(censor("The code is fourty"))
