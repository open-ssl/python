def initialisator(func):
    def inner_func(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner_func


# def subgen():
#     x = 'Ready to accept message'
#     message = yield x
#     print('Show text for user', message)


class BlaBlaException(Exception):
    pass
#
# @initialisator
# def average():
#     count = 0
#     summ = 0
#     average = None
#     while True:
#         try:
#             x = yield average
#         except StopIteration:
#             print('Done')
#         except BlaBlaException:
#             print('Done')
#         else:
#             count += 1
#             summ += x
#             average = round(summ / count, 2)
#     return average
#


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            print('had Exception')
            break
        else:
            print(".......", message)
    return 'result111'

@initialisator
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    # consist creating subgen, so we don't need decorator by pep380
    result = yield from g
    print(result)
