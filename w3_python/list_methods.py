# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# конструктор списка list() создает новую ячейку памяти

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)
#
#
# thislist = ["apple", "banana", "cherry", "banana"]
# thislist.remove("banana")
# print(thislist)
# thislist.remove("banana")
# print(thislist)


thislist = ["apple", "banana", "cherry"]
# delete index
# del thislist[2]

# no matter
# delete all list
# del thislist
# thislist.clear()

# print(thislist)



# Копирование списка
# Нельзя просто написать copy1 = copy2 потому что они всё ещё ссылаются на одну
# область памяти и изменения в одном списке повлекут изменения в другом
# ДВА ПУТИ

lst1 = ['stas']
# 1. безопасно копируем методом copy()
lst2 = lst1.copy()
# 2. Метод list() создаёт новую ячейку памяти
lst3 = list(lst2)

#  Да, у них все в порядке с содержимым
print(lst1 == lst2 == lst3)
#  Но ссылаются они на разные места, что хорошо
print(lst1 is lst2 is lst3)


# объединяем списки

# обычная конкатенация
lst1 + lst2

# итерируемся по одному списку и добавляем в другой
# for i in lst1:
#     lst2.append()


# специальный метод
lst3 = [1, 2, 3, 5]
lst4 = [6, 7, 8, 10]
lst3.extend(lst4)
# print(lst3)

# SHOK
#  список наоборот, альтернатива  [::-1]
# print(lst3[::-1])
lst3.reverse()
# print(lst3)
lst3.sort()

# функция sorted работает также как и метод sort
print(lst3)
print(sorted(lst3))

# to position
# lst.insert(10)

# remove Item
# lst.remove('aaa')
