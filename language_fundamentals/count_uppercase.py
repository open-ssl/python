# def count_uppercase(lst):
# 	return sum(letter.isupper() for letter in [word for word in lst])


def count_uppercase(lst):
    return sum(letter.isupper() for word in lst for letter in word)

print(count_uppercase(["EDAbit", "Educate", "Coding"]))



# print([i for i in 'stas'])
