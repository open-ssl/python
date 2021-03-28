# исключения
# try:
#     print('saaaaa')
#     raise Exception()
# except:
#     print('asdada')
# # если эксепт не сработал
# else:
#     print('nm')
# finally:
#     print('lie1')


# создаём своё

class MyError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        print('aa1')


# создаём пользовательское исключение
try:
    raise Exception('aaa')
except Exception as e:
     MyError('message', 'info')
