# Date

from datetime import datetime
print(datetime.today())
print(f'{datetime.today():%B %d %m %y}')


# Строки
a = 123
my = 'aaaaa'

# это называется F строки
# print(f'Stas {a}, {my}')
# print(f'Stas {a:.3f}, {my:10s}')

# Библиотеки
import logging

logging.debug('ok')

logging.warning('AAAAA')


import os
# print(os.getenv('PATH'))

import json

lst = list([{'hello': [1, 2, None, 3, "stas"]}])

a = json.dumps(lst)
print(a)
# if __name__ == "__main__":
	# print('hello')


# почитать количество объектов
from collections import Counter, OrderedDict

cnt = Counter([1, 2, 3, 3, 3, 3, 3,3 , 3, 3 ,3 ,3 , 3, 3, 3, 3])
cnt_str = Counter('My name is Stanislav')
# количество элементов и их ключи в алфавитном порядке
cnt2 = Counter(a=2, c=3, d=5)
print(sorted(cnt2.elements()))
print(cnt2)

# print(cnt[3])
# print(cnt)
print(cnt2.most_common(1))



# словарь который хранит элементы в том порядке в каком они в него пришли
od = OrderedDict({'stas': 1})
od.update({'new': 213})
# сдвигает выбранный ключ в словаре. Имеет 2 аргумент last=True
od.move_to_end('stas')
print(od)

# map выполняет функцию ко всем элементам итерирумого объекта
# filter выполняет функцию ко всем элементам итерирумого объекта оставляя лишь те элементы которые прошли проверку (2 аргумент)
# reduce импортится из collection , выполняет функцию аккумулятивно по всем элементам итерирумого объекта



# метод dir показывает содержимое в атрибутах и методах класса
dir(list)


# чтобы создать объект нового типа нужно создать класс и занасаследовать его от базового типа object

class NewType(object):
    pass


#  WriteOnCopy

a1 = 23
# a2 будет ссылаться на ту же область памяти что и a1
a2 = a1

# выведутся два одианаковых значения переменных лежащих в одной области памяти
print(a1)
print(a2)

# впервые поменяли значение a2. Под неё сразу выделилась своя область памяти
a2 = 24
# выведутся два разных значения переменных лежащих в разных областях памяти
print(a1)
print(a2)


# функция repr отличается от функции int
# int округляет объект в то время как repr показывает как объект представлен в памяти компьютера

# Литералы

# Числовые 4 типа
# Булевы значения
# Числа с точкой
# Комплексные
# Дробные


# строковые

# Сырые строки, такие строки, в которых не работают символы литералов, а воспринимаются как обычный текст записываются как:
# r'\n'
# Полезно например для
# r’c:\newdata\tests’
