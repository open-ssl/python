'''
Write a function that recursively returns the number of vowels in a string.

If it wasn't clear enough already, you should use recursion in your solution.

Examples
vowels("apple") ➞ 2

vowels("cheesecake") ➞ 5

vowels("bbb") ➞ 0

vowels("") ➞ 0
'''

lst_vovels = [i for i in 'euioa']
def func(local_str):
    return int(local_str in 'euioa')

def vowels(string):
    return func(string[len(string)-1]) + vowels(string[:len(string)-1]) if len(string) > 0 else func(string)


print(vowels(''))
