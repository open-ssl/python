'''
Create a function that counts how many characters make up a rectangular shape. You will be given a list of strings.
'''

def count_characters(lst):
    return sum(len(i) for i in lst)


print(count_characters([
  "###",
  "###",
  "###"
]))

'''
count_characters([
  "###",
  "###",
  "###"
]) ➞ 9

count_characters([
  "22222222",
  "22222222",
]) ➞ 16

count_characters([
  "------------------"
]) ➞ 18

count_characters([]) ➞ 0

count_characters(["", ""]) ➞ 0
'''
