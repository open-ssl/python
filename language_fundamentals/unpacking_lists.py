'''
For each challenge of this series you do not need to submit a function.
Instead, you need to submit a template string that can be formatted in order to get a certain outcome.
Write three lists and a template string according to the following example. Notice the keyword argument elem:
'''

lst1 = ['John', 'Joe', 'Jack']
lst2 = ['E', 'da', 'bit']
lst3 = ['Metapod', 'Magikarp', 'Unown']
template = "My {elem} are: {}, {} and {}."

# template.format(*lst1, elem="friends") ➞ "My friends are: John, Joe and Jack."
# template.format(*lst2, elem="loves") ➞ "My loves are: E, da and bit."
# template.format(*lst3, elem="pokemon") ➞ "My pokemon are: Metapod, Magikarp and Unown."

print(template.format(*lst1, elem="friends"))
