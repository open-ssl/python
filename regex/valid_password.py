# Exactly 4 or 6 characters.
# Only numerical characters (0-9).
# No whitespace.

import re
import unittest
def func(txt):
    is_ok_len = 3 < len(txt) < 7
    is_just_nums = not bool(re.search('\D', txt))
    is_space_not_in = not bool(re.search('\s', txt))
    return is_ok_len and is_just_nums and is_space_not_in


class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(func('1235s'), False)

    def test2(self):
        self.assertEqual(func('1235 '), False)

    def test3(self):
        self.assertEqual(func('1235232323'), False)


if __name__ == '__main__':
    unittest.main()
