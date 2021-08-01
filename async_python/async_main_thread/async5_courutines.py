# from inspect import getgeneratorstate


class BlaBlaExeption(Exception):
    pass


def corutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner
# корутины, это те же самые генераторы,
# которые в процессе работы могут принимать извне какие-то данные
# с помощью метода send


def subgen():
    x_variable = 'Ready for access'
    message = yield x_variable
    print('Subgen received', message)

@corutine
def average():
    count, summ, average = 0, 0, None
    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
        except BlaBlaExeption:
            print('arrr')
        else:
            count += 1
            summ += x
            average = round(summ / count)
    return average


# Correct order
# type
# g = subgen()
# getgeneratorstate(g)   'GEN_CREATED'
# передали None - это обязательное действие,
# которое предписано документацией
# type
# g.send(None)
# генератор приостановлен
# type
# getgeneratorstate(g)   'GEN_SUSPENDED'
# type
# g.send('Send text')
###
# Если в генераторе происходит return и происходит возврат некоторых значений,
# то при возбуждении исключения через throw, можно перехватить исключение и в
# атрибуте value будет лежать значение из return
