
# list comprehension (list generator)
lst = ["stas" ,"ssda"]
print([char for item in lst for char in item])


lst0 = [1, 2, 3, 4]

# link to lst0
lst1 = lst0
lst1.append(5)
# [1, 2, 3, 4, 5]
print(lst0)
# [1, 2, 3, 4, 5]
print(lst1)

# change link for object lst1 to new part of item
lst1 = [6, 7, 8, 9]
# [6, 7, 8, 9]
print(lst1)
# [1, 2, 3, 4, 5]
print(lst0)


set1 = {i: i**2 for i in [10, 10, 11, 11, 12, 12]}
print(set1)



# generator REAL generator with ( )
print((i for i in range(20)))


# generator
b = (i * 0.33 for i in range(4))
for i in b:
    print(i)


def func(number):
    while number < 10:
        yield number
        number += 1


tmp = func(3)
for i in tmp:
    print(i)
