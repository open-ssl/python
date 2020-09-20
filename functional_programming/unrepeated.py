'''

Create a function that will remove any repeated charcter(s) in a word passed
to the function. Not just consecutive characters, but characters
repeating anywhere in the input.
'''

def unrepeated(txt):
    return ''.join([txt[i] for i in range(len(txt)) if txt[:i+1].count(txt[i]) < 2])

# def unrepeated(txt):
#     j = txt[0]
#     new_txt = j
#     for i in range(1, len(txt)):
#         if txt[i] != j:
#             new_txt += txt[i]
#             j = txt[i]
#     return new_txt
#
#
# print(unrepeated("hello"))
# print(unrepeated("WWE!!!"))
# '''
#
#
# unrepeated("aaaaa")  "a"
#
# unrepeated("WWE!!!")  "WE!"
#
# unrepeated("call 911")  "cal 91"
# '''

print(unrepeated("call 911"))
