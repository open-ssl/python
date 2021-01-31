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
    from datetime import date
    from time import gmtime, strftime
    database_name = 'bot.db'
    connect_obj = SQL_Main(database_name)
    time_from_hours, time_to_hours, time_from_min, time_to_min = connect_obj.get_time_borders(user_id)
    working_days_list = connect_obj.get_working_days(user_id)
    user_utc_time = int(connect_obj.get_user_utc_time(user_id))
    working_days_list = [int(i) for i in working_days_list[0][1:-1].split(', ')]
    server_ymd = strftime("20%y %m %d")
    server_time = strftime("%H %M")
    server_time_zone = int(strftime("%z", gmtime())[2])
    y, m, d = server_ymd.split(' ')
    server_date = date(int(y), int(m), int(d))
    server_weekday = server_date.weekday() + 1
    user_server_diff = user_utc_time - server_time_zone
    h, m = server_time.split(' ')
    h, m = int(h), int(m)
    user_real_h = h + user_server_diff
    user_real_m = m
    if user_real_h > 23:
        user_real_h = user_real_h - 24
    if user_real_h not in (time_from_hours, time_to_hours):
        # Временной диапазон где мы можем отправлять сообщение
        # вызов функции которая проверяет когда в последний раз бот отправил пользователю сообщение третье условие
        print(1)
        return user_real_h > time_from_hours and user_real_h < time_to_hours
    else:
        # мы в пограничном часе. Проверяем минуты
        # вызов функции которая проверяет когда в последний раз бот отправил пользователю сообщение второе условие
        if user_real_h == time_from_hours:
            print(3)
            return user_real_m > time_from_min
        print(4)
        return user_real_m < time_to_min


    # сделано
    # if server_weekday in working_days_list
        # если текущий день на сервере не совпадает с пользовательскими чилим

    connect_obj.close()

    # server_hour, server_min =
    # 0. вытащить текущий день на сервере если он не совпадает с нашим чилим
    # 1. чекнуть текущее время на сервере с учетом пояса,
    # 2. вытащить часовой пояс юзера привести время с сервера к времени пользователя
    # return time_from, time_to

'''
from datetime import date
from time import gmtime, strftime
ymd = strftime("20%y %m %d")
y, m, d = ymd.split(' ')
server_date = date(int(y), int(m), int(d))
print(server_date.weekday() + 1)
'''
# b = strftime("%H %M")
# a = strftime("%z", gmtime())
#????
from datetime import datetime
from time import gmtime, strftime
# # получить текущее время на сервере
print(time_checker())



# server_time = strftime("%H %M")
# server_time_zone = int(strftime("%z", gmtime())[2])
#
# # с этого момента
# user_utc_time, lst, user_hm_info = time_checker()
# user_utc_time = int(user_utc_time)
# user_server_diff = user_utc_time - server_time_zone
# h, m = server_time.split(' ')
# h, m = int(h), int(m)
#
# # получаем реальное время пользователя по utc
# user_real_h = h + user_server_diff
# user_real_m = m
# if user_real_h > 23:
#     user_real_h = user_real_h - 24
#
# if user_real_h not in (user_hm_info[0], user_hm_info[1]):
#     # Временной диапазон где мы можем отправлять сообщение
#     # вызов функции которая проверяет когда в последний раз бот отправил пользователю сообщение третье условие
#     return user_real_h > user_hm_info[0] and user_real_h < user_hm_info[1]:
# else:
#     # мы в пограничном часе. Проверяем минуты
#     # вызов функции которая проверяет когда в последний раз бот отправил пользователю сообщение второе условие
#     if user_real_h == user_hm_info[0]
#         return user_real_m > user_hm_info[2]
#     return user_real_m < user_hm_info[3]


# if server_time_zone + user_utc_time  > 23:
    # выходим
    # pass



# user_server_time

# print(int(server_time_zone))
# print(user_utc_time)
# print(type(user_utc_time))
