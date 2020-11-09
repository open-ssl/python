# итератор
# объект который позволяет по ссылке на итерируеумый объект переходить к элементам
# обязательно должен иметь методы iter и next


# class MyIterator:
#     def __init__(self, last_value):
#         self.last_value = last_value
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def next(self):
        # if self.counter == 0:
        #     raise StopIteration
        # self.counter -= 1
        # return self.counter
#
# mi = MyIterator(10).__iter__()
# mi.next()
# mi.next()
# mi.next()
# mi.next()
# mi.next()
# mi.next()
# mi.next()
# mi.next()
# mi.next()
# mi.next()
# mi.next()


######################################################

# создаем свой итератор встроенной функцией iter
new_iter = iter([1, 2, 3, 4])

# <class 'builtin_function_or_method'>
# print(type(iter))

# имеем тип итератор
# <class 'list_iterator'>
print(type(new_iter))


print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
# print(type(next(new_iter)))



######################################################

# создаём свой генератор
# генератор это инструмент для создания итераторов
# по сути это функция, которая возвращает yield вместо return в место вызова
print('')
def reverse(data):
    for i in range(len(data)-1, -1, -1):
        # возвращаем итератор в место вызова
        # сохрани и вызови результат операции
        yield data[i]


for char in reverse('ahahahahe'):
    print(char)
