'''
Create a function that will remove any repeated charcter(s) in a word passed to the function.
'''
# def unrepeated(txt):
#     count = 0
#     while count +1 < len(txt):
#         if txt[count] == txt[count+1]:
#             txt = txt.replace(txt[count], '')
#         else:
#             count += 1
#     return txt

def unrepeated(txt):
    for i in txt:
        if txt.count(i) > 1:
            while txt.count(i) != 1:
                txt = txt[:txt.rfind('a')] + txt[txt.rfind('a')+1:]
    return txt

print(unrepeated("altwaff test"))


# altwaff test, "altwf es
