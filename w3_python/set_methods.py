#  Cет неупорядочен. Нельзя получить элементы никак но можно проитерировать по нему
thisset = {"apple", "banana", "cherry"}
print(thisset)



# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop,
# or ask if a specified value is present in a set, by using the in keyword.


thisset = {"apple", "banana", "cherry"}

# add 1 element
thisset.add('new_item')
# many
thisset.update(["orange", "mango", "grapes"])
# remove will give raise if no element
thisset.remove("banana")
# discard will no give raise if no element
thisset.discard("banana")

# pop remove last item in set. Set is ONORDERED so we cant know what it will element
thisset.pop()
print(thisset)

# remove all in set
thisset.clear()

# print(thisset)


# concat two sets


set1 = {'stas', 'ss', 'aaa'}
set2 = {'stasyan', 'ss11', 'aaa222'}

# 1. Union return new set
# set3 = set1.union(set2)

# 2. update() will change current set
# set1.update(set2)
# print(set1)

# EQUAL
# print(set1 & set2)
# set3 = set1.intersection(set2)
# print(set3)

# EQUAL
# print(set1 | set2)
# set3 = set1.union(set2)
# print(set3)

# Equal
# print(set1 ^ set2)
# set3 = set1.difference(set2)
# print(set3)
