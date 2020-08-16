import re
import unittest

'''
Create a regular expression to check whether the given string
is a valid floating numeric character or not.
'''

def is_float_number(aa):
    return bool(re.match('[\+-]*\d*\.\d+$', aa))

class Test(unittest.TestCase):
    def test1(self):
        return self.assertEqual(is_float_number("12.12"), True)
    def test2(self):
        return self.assertEqual(is_float_number("12."), False)
    def test3(self):
        return self.assertEqual(is_float_number(".1"), True)
    def test4(self):
        return self.assertEqual(is_float_number("-.1"), True)
    def test5(self):
        return self.assertEqual(is_float_number("+4.4"), True)
    def test6(self):
        return self.assertEqual(is_float_number("+4"), False)
    def test7(self):
        return self.assertEqual(is_float_number("+4.4av"), False)

if __name__ == '__main__':
    unittest.main()
