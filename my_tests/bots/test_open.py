# тестирование чтения инфы из файла

# with open('/Users/stanislavlukanov/Desktop/LEARN/python/python/my_tests/bots/en_words/level1.txt', 'r') as f:
#     file = f.readlines()
#     for row in file:
#         key, word = row.split(' ')
#         print(key)
#         print(word)


#


# приведение дней недели к нормальному числовому виду
# print([int(i) for i in '[1, 2, 3, 4, 5]'[1:-1].split(', ')])

from sql.classes import SQL_Main
import time

def time_checker(user_id):
    """
        Проверяет, можно ли отправить пользователю очередное сообщение
    """
    database_name = 'bot.db'
    connect_obj = SQL_Main(database_name)
    time_from, time_to = connect_obj.get_time_borders(user_id)
    connect_obj.close()
    # return time_from,time_to
    # чекнуть время


print(time_checker())
