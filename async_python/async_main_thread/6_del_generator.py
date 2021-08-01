# from inspect import getgeneratorstate


def corutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner
# корутины, это те же самые генераторы,
# которые в процессе работы могут принимать извне какие-то данные
# с помощью метода send


class BlaBlaExeption(Exception):
    pass

#
# def subgen():
#     for item in 'stas':
#         yield item
#
#
# def delegator(g):
#     for item in g:
#         yield item

def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            print('qq!!!!')
            break
        else:
            print('Catched message is: ', message)
    return 'Return from Subgen'

@corutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaExeption as e:
    #         g.throw(e)
    # одной строкой заменили все что выше
    result = yield from g
    print(result)
