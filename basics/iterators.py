from datetime import datetime


# Итератор имеет 2 метода __init__ и next()

class MyIterator:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.j:
            ret_val = self.i
            self.i += 1
            return ret_val
        else:
            raise StopIteration("No more elements")

# it = MyIterator(10, 20)


'''
lst = [i for i in range(100)]

start =  datetime.now()
for i in lst:
    print(i)

end1 = datetime.now() - start

lst = lst.__iter__()

start = datetime.now()
for i in lst:
    print(lst.next())

end2 = datetime.now() - start

# 0:00:00.000507
print(end1)
# 0:00:00.000199
print(end2)
'''
# my_map = filter(lambda x: x%2, [i for i in range(10)])
# my_filter = map(lambda x: x*2, [i for i in range(10)])
# my_enumerate = enumerate([i for i in range(10)])
# print(type(my_filter))
# print(my_filter)
# print(type(my_map))
# print(my_map)
# #
# for i, j in enumerate([10, 20, 30]):
#     print(i, j)
#
# for i in my_map:
#     print(my_map.next())
#
# import itertools
# it = itertools.combinations('ABCD', 2)
#
# for i in it:
#     print(it.next())
# it = itertools.compress('ABCDEF', [1,0,1,0,1,1])

# from itertools import chain

# it1 = iter([1,2,3])
# it2 = iter([8,9,0])
# for i in chain(it1, it2):
  # print(i)


# print(itertools.accumulate([1,2,3,4,5]))



lst = [i for i in range(100)]

for i in lst:
    print(i)



# lst = iter(lst)

# for i in lst:
    # next(lst)



class MyIterator:
    
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0


    def __iter__(self):
        return self

    def next(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


#
# iter111 = MyIterator(5)
#
# for i in iter111:
#     print(i)
