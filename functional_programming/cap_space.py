'''
Create a function which adds spaces before every capital in a word. Uncapitalize the whole string afterwards.
'''


import re
def cap_space(txt):
    return re.findall('[a-z]+', txt)[0] + ' '
            + ' '.join(re.findall('[A-Z][a-z]+', txt)).lower()

print(cap_space("iLoveMyTeapot"))
# cap_space("helloWorld") ➞ "hello world"

# cap_space("iLoveMyTeapot") ➞ "i love my teapot"

# cap_space("stayIndoors") ➞ "stay indoors"
