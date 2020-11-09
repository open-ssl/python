def first_non_repeated_character(txt):
    lst = [i for i in txt if txt.count(i) == 1]
    return lst[0] if lst else False

print(first_non_repeated_character("g"))
 # ➞ "g"

print(first_non_repeated_character("it was then the frothy word met the round night"))
 # ➞ "a"

# first_non_repeated_character("the quick brown fox jumps then quickly blows air") ➞ "f"

# first_non_repeated_character("hheelloo") ➞ False

print(first_non_repeated_character(""))
