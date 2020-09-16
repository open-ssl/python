'''
Lets assume for the purposes of this challenge that
for every layer of fabric you wear when it's cold outside
(coats, cardigans, etc), the temperature increases by a tenth of the total.

Given n number of layers and a given temperature,

return the temperature inside of all those warm fuzzy layers.
Round to the nearest tenth of a degree.
'''

# import re
def calc_bundled_temp(n, temp):
    return str(round(1.1 ** n * int(temp.split('*')[0]), 1)) + '*C'

calc_bundled_temp = lambda n, temp:
# print(calc_bundled_temp(2, "10*C"))
#
# print(calc_bundled_temp(4, "6*C"))
#
# # calc_bundled_temp(20, "4*C")

# calc_bundled_temp(1, "2*C") ➞ "2.2*C"

# calc_bundled_temp(4, "6*C") ➞ "8.8*C"

# calc_bundled_temp(20, "4*C") ➞ "26.9*C"
