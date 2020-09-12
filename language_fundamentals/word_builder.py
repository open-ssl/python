
def word_builder(lst1, lst2):
    return ''.join([lst1[i] for i in lst2])
    # return ''.join([i[0] for i in sorted(zip(lst1, lst2), key=itemgetter(1))])

print(word_builder(["g", "e", "o"], [1, 0, 2]))

print(word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]))
 # ➞ "test"

print(word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2]))
# ➞ "edabit"
