'''
Write a function that changes every letter to the next letter:

"a" becomes "b"
"b" becomes "c"
"d" becomes "e"
and so on ...
'''

# ord('z') == 122
def move(string):
    return ''.join(chr(ord(i)+1) for i in string)



print(move('hello'))
# move("hello") ➞ "ifmmp"

# move("bye") ➞ "czf"
#
# move("welcome") ➞ "xfmdpnf"
