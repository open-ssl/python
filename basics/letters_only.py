def letters_only(txt):
    txt = ''.join(i for i in txt.split())
    return txt.islower() and txt.isalpha()


# letters_only("PYTHON") ➞ false

print(letters_only("python"))
 # ➞ true

print(letters_only("12321313"))
# ➞ false

print(letters_only("i have spaces"))
 # ➞ true

print(letters_only("i have numbers(1-10)"))
 # ➞ false

print(letters_only(""))
 # ➞ false
