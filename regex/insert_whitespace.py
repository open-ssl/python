import re
import unittest

'''
Write a function that inserts a white space between every instance
of a lower character followed immediately by an upper character.
'''
def insert_whitespace(txt):
     return ' '.join(list(re.findall(r"[A-Z][a-z]*", txt)))

class TestMethod(unittest.TestCase):
    def test1(self):
        self.assertEqual(insert_whitespace("SheWalksToTheBeach"),  "She Walks To The Beach")
    def test2(self):
        self.assertEqual(insert_whitespace("MarvinTalksTooMuch"),  "Marvin Talks Too Much")
    def test3(self):
        self.assertEqual(insert_whitespace("TheGreatestUpsetInHistory"),  "The Greatest Upset In History")

if __name__ == '__main__':
    unittest.main()

# insert_whitespace("SheWalksToTheBeach") ➞ "She Walks To The Beach"
# insert_whitespace("MarvinTalksTooMuch") ➞ "Marvin Talks Too Much"
# insert_whitespace("TheGreatestUpsetInHistory") ➞ "The Greatest Upset In History"
