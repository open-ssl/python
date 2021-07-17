# for i in range(5):
#     print(i)

_iter = range(5).__iter__()
while 1:
    try:
        print(_iter.__next__())
    except StopIteration:
        break
