'''
Given a string, reverse all the words which have odd length. The even length words are not changed.
'''



def reverse_odd(txt):
    return ' '.join(i[::-1] if len(i) % 2 else i for i in txt.split())


# print(reverse_odd("Bananas"))

# reverse_odd("One two three four")  "enO owt eerht four"

print(reverse_odd("Make sure uoy only esrever sdrow of ddo length"))
#  "Make sure you only reverse words of odd length"
