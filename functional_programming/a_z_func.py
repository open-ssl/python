'''
Given a string indicating a range of letters, return a string which
includes all the letters in that range, including the last letter.
Note that if the range is given in capital letters,
return the string in capitals also!
'''


def gimme_the_letters(txt):
    return ''.join(chr(i) for i in range(ord(txt[0]), ord(txt[2])+1))

print(gimme_the_letters("a-z"))
  # "abcdefghijklmnopqrstuvwxyz"

# gimme_the_letters("h-o")  "hijklmno"

# gimme_the_letters("Q-Z")  "QRSTUVWXYZ"

print(gimme_the_letters("J-J"))
  # J"
