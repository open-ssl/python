def shared_letters(str1, str2):
    return sum(i in set(str2) for i in set(str1))
print(shared_letters("apple", "meaty"))
 # ➞ 2
# Since "ea" is shared between "apple" and "meaty".

print(shared_letters("fan", "forsook"))
 # ➞ 1

shared_letters("spout", "shout")
 # ➞ 4
