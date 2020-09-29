# tuples methods
import datetime

# new tuple is object
# tuple(())
# нельзя никак менять элементы кортежа, но можно удалить его целиком

t1 = tuple(range(1, 200))
l1 = list(range(1, 200))

s1 = datetime.datetime.now()
for i in t1:
    pass
tmp1 = datetime.datetime.now() - s1


s2 = datetime.datetime.now()
for i in l1:
    pass
tmp2 = datetime.datetime.now() - s2

print(tmp1)
print(tmp2)


# Если очень нужно поменять кортеж приводим к словарю и меняем
x = ("apple", "banana", "cherry")
# print(x[0])
y = list(x)
y[1] = "kiwi"
x = tuple(y)



# !!! (tuples are unchangeable)


# tuple with 1 item

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


del thistuple

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# TWO methods

thistuple.index()
thistuple.count()
