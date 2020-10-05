def duplicate_count(txt):
    return len(set(i for i in txt if txt.count(i) > 1))



print(duplicate_count("abcde"))
 # ➞ 0
print(duplicate_count("aabbcde"))

print(duplicate_count("Indivisibilities"))
 # ➞ 2

# duplicate_count("Aa") ➞ 0
