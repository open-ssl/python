'''
The challenge is to recreate the functionality of the title() method into
a function called emphasise(). The title() method capitalises the first letter of every word.
'''

def emphasise(txt):
    return ' '.join([item[0].upper() + item[1:] for item in txt.lower().split(' ')])


print(emphasise(""))


'''
emphasise("hello world") ➞ "Hello World"

emphasise("GOOD MORNING") ➞ "Good Morning"

emphasise("99 red balloons!") ➞ "99 Red Balloons!"
'''
