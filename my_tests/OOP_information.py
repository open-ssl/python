class Parent:
    help = 'help'

    def __init__(self):
        print('some')

class Child(Parent):
    def __init__(self):
        print('some')

print("=========")
child = Child()
# эта переменная здесь есть потому что объявлена на уровне класса
# имеем простой пример наследования
print(child.help)

######################################
class Dog:
    def __init__(self):
        self.func = '2'

def my_func(arg1):
    return arg1 + ' aaaaa'



hot_dog = Dog()
# пример композиции
# ибо я расширяю функциональность класса за счёт функции

hot_dog.func = my_func
######################################

a = 2
b = 3
c = 'Stas'
d = ' Lukyanov'

# примеры полиморфизма
# результат выполнения некоторой операции будет различаться
# и зависеть от объектов для которых этот полиморфизм применен
print(a + b)
print(c + d)
######################################

class MyNew():

    # статический метод
    # может не использовать ссылку на объект self.  
    # вызывается по имени класса или от экземляра объекта

    @staticmethod
    def my_method():
        return 'It is okay'

    # обычный метод класса
    # всегда вызывается от объекта класса
    def my_method2(self):
        return '222'



new = MyNew()
# print(MyNew()._MyNew__my_method())

print(new.my_method())
print(MyNew.my_method())
print(new.my_method2())
# тут ошибка т.к. MyNew не экземпляр
# print(MyNew.my_method2())
# а тут всё окей т.к. я сделал экземпляр MyNew()
print(MyNew().my_method2())


######################################


class AnotherOne():
    @classmethod
    def get_model(cls):
        print('This is class {0}'.format(cls.__name__))
        return cls


ao = AnotherOne()
# метод класса берет аргументом ссылку на
# объект класса и позволяет брать из него методы и атрибуты
print(ao.get_model())

######################################




class Property():
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    # делаем метод атрибутом
    @property
    def property_method(self):
        return self.arg1 + self.arg2



prop = Property(100, 1)
print(prop.property_method)
######################################
