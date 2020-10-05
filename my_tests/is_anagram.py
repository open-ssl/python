import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(is_anagram("cristian", "Cristina"), True)
    def test2(self):
        self.assertEqual(is_anagram("Dave Barry", "Ray Adverb"), True)
    def test3(self):
        self.assertEqual(is_anagram("Nope", "Note"), False)


def is_anagram(txt1, txt2):
    return sum([ord(i) for i in txt1.lower()]) == sum([ord(i) for i in txt2.lower()])

print(is_anagram("cristian", "Cristina"))
 # ➞ True

print(is_anagram("Dave Barry", "Ray Adverb"))
 # ➞ True

print(is_anagram("Nope", "Note"))
 # ➞ False
if __name__=="__main__":
    unittest.main()
