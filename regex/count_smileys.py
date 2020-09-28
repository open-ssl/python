import re
import unittest
'''
Create a function that takes a list of strings and return the number of smiley faces contained within it. These are the components that make up a valid smiley:

A smiley has eyes. Eyes can be : or ;.
A smiley has a nose but it doesn't have to. A nose can be - or ~.
A smiley has a mouth which can be ) or D.
No other characters are allowed except for those mentioned above.
'''
def count_smileys(lst):
    return len(list(re.findall('[:;][-~]{1}[)D]', str(lst))))

# print(count_smileys([";]", ":[", ";*", ":$", ";-D"]))

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(count_smileys([":)", ";(", ";}", ":-D"]), 2)
    def test2(self):
        self.assertEqual(count_smileys([";D", ":-(", ":-)", ";~)"]), 3)
    def test3(self):
        self.assertEqual(count_smileys([";]", ":[", ";*", ":$", ";-D"]), 1)

if __name__ == '__main__':
    unittest.main()

# count_smileys([":)", ";(", ";}", ":-D"]) 2
# count_smileys([";D", ":-(", ":-)", ";~)"])  3
# count_smileys([";]", ":[", ";*", ":$", ";-D"])  1
