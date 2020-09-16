'''
boom_intensity(4)  "Boooom!"
# There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)

boom_intensity(1)  "boom"
# 1 is lower than 2, so we return "boom"

boom_intensity(5)  "BOOOOOM"
# There are 5 "o"s and 5 is divisible by 5 (all caps)

boom_intensity(10)  "BOOOOOOOOOOM!"
# There are 10 "o"s and 10 is divisible by 2 and 5 (all caps and exclamation mark included)
'''


'''
Given a number, return a string of the word "Boom", which varies in the following ways:

The string should include n number of "o"s, unless n is below 2 (in that case, return "boom").
If n is evenly divisible by 2, add an exclamation mark to the end.
If n is evenly divisible by 5, return the string in ALL CAPS.
The example below should help clarify these instructions.
'''

def boom_intensity(n):
    if n < 2:
        return 'boom'
    return_value = "B{}m".format(n*'o')
    if not n % 2:
        return_value +='!'
    if not n % 5:
        return_value = return_value.upper()
    return return_value

print(boom_intensity(10))
print(boom_intensity(5))
print(boom_intensity(4))
print(boom_intensity(2))
