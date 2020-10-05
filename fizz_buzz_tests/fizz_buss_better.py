# # объект который позволяет по ссылке на итерируеумый объект переходить к элементам
# # обязательно должен иметь методы iter и next
#
#
# class MyIterator:
#     def __init__(self, last_value):
#         self.last_value = last_value
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.last_value != self.counter:
#             print(self.counter)
#             self.counter+=1
#         else:
#             raise StopIteration('The end')
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
#
#

def func(value):
    for i in range(1, 101):
        res_text = ['', 'fizz'][i % 3 == 0]
        res_text += ['', 'buzz'][i % 5 == 0]
        print(res_text) if res_text else print(i)

func(100)
