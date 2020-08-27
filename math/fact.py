'''
Write a function that finds the longest word in a sentence.
If two or more words are found, return the first longest word.
Characters such as apostophe, comma, period (and the like) count as part of the word (e.g. O'Connor is 8 characters long).
'''

def longest_word(txt):
    lst = [len(item) for index, item in enumerate(txt.split(' '))]
    return txt.split(' ')[lst.index(max(lst))]


# longest_word("Hello darkness my old friend.") ➞ "darkness"
# longest_word("Hello there mate.") ➞ "Hello"
# longest_word("Margaret's toy is plastic.") ➞ "Margaret's"
