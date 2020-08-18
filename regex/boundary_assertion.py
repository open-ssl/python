import re
import unittest

'''
Given a sentence spelling out a word, return True
if the spelled letters match the word at the end of the string.
'''

def validate_spelling(txt):
    return ''.join(i for i in re.split('\.\s', txt.lower())[:-1]) in txt.lower()


print(validate_spelling('C. Y. T. O. P. L. A. S. M. Cytoplasm?'))
print(validate_spelling('P. H. A. R. A. O. H. Pharaoh!'))
print(validate_spelling('H. A. N. K. E. R. C. H. E. I. F. Handkerchief.'))

# validate_spelling("C. Y. T. O. P. L. A. S. M. Cytoplasm?") ➞ True
# validate_spelling("P. H. A. R. A. O. H. Pharaoh!") ➞ True
# validate_spelling("H. A. N. K. E. R. C. H. E. I. F. Handkerchief.") ➞ False
