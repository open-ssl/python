import sqlite3
import weakref
import schedule
import time
import telebot
import numpy as np
import json


class SQL_Main:
    """
    Класс получения информации из базы
    """
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()


    def select_word(self):
        """ Получаем все строки """
        with self.connection:
             obj = self.cursor.execute('SELECT * FROM level1_table').fetchall()
             return obj


    def add_new_user(self, chat_id, username):
        with self.connection:
            print('chat_id!!!')
            print(chat_id)
            # (user_id integer, level_id integer user_name text)
            # obj = self.cursor.execute("SELECT 1 FROM user_table WHERE user_id = ?", chat_id)
            obj = self.cursor.execute('SELECT 1 FROM user_table WHERE user_id = ?', (chat_id,)).fetchall()
            if not obj:
                self.cursor.execute("INSERT INTO user_table VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (chat_id, 1, username, '0', 10, 17, json.dumps([1,2,3,4,5]), 25))
                self.connection.commit()
                print('ADDED USER IN TABLE')


    def rename_user(self, chat_id, new_username):
        with self.connection:
             # (user_id integer, level_id integer user_name text)
            self.cursor.execute("UPDATE user_table SET user_name = ? where user_id = ?", (new_username, chat_id, ))
            self.connection.commit()
            print('RENAME USER IN TABLE')


    def set_user_time(self, chat_id, user_time):
        with self.connection:
            # (user_id integer, level_id integer user_name text)
            self.cursor.execute("UPDATE user_table SET user_time = ? where user_id = ?", (user_time, chat_id, ))
            self.connection.commit()
            print('SET USER TIME IN TABLE')

    def get_all_user(self):
        with self.connection:
            obj = self.cursor.execute('SELECT * FROM user_table').fetchall()
            print(obj)

    def get_time_borders(self, user_id):
        with self.connection:
            time_obj = self.cursor.execute('SELECT time_from, time_to FROM user_table WHERE user_id = ?', (user_id,)).fetchall()
            return (time_obj[0][0], time_obj[0][1])

    def close(self):
        self.connection.close()


class SQL_ConnectTable:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        # self.cursor.execute("""DROP TABLE IF EXISTS connect_table
        #            """)
        #
        # self.cursor.execute("""CREATE TABLE connect_table
        #           (connect_id integer, connect_name text)
        #        """)

    def ct_close(self):
        self.connection.close()




class SQL_Level1_Table:

    def __init__(self, database=None):
        if not database:
            return
        self.database = database
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""DROP TABLE IF EXISTS level1_table
                   """)

        self.cursor.execute("""CREATE TABLE level1_table
                  (id integer, word text, translate text, sound text)
               """)
        print('level1_table table was created)))')


    def set_level1(self):
        with self.connection, \
            open('/Users/stanislavlukanov/Desktop/LEARN/python/python/my_tests/bots/en_words/level1.txt', 'r') as f:
            file = f.readlines()
            for it, row in enumerate(file):
                word, translate = row.split(' ')
                self.cursor.execute("INSERT INTO level1_table VALUES(?, ?, ?, ?)", (it, word, translate, ' '))
                self.connection.commit()
            print('LEVEL 1 WAS CREATED')


    def get_level1_words_count(self):
        "Смотрим сколько записей в таблице"
        self.connection = sqlite3.connect(self.database)
        with self.connection:
            a = self.cursor.execute("""Select * from level1_table""").fetchall()
            return len(a)

    def close(self):
        self.connection.close()


class SQL_UserTable:
    "Таблица юзеров"

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""DROP TABLE IF EXISTS user_table
                   """)

        self.cursor.execute("""CREATE TABLE user_table
                  (user_id integer, level_id integer, user_name text, user_time text, time_from integer, time_to integer, days array integer, interval integer)
               """)

    def close(self):
        self.connection.close()


class UserCache:
    def __init__(self, cacheSize):
        self.cache = {}
        self.cache_LRU = []
        self.cacheSize = cacheSize

    def __getitem__(self, key):
        value = self.cache[key]
        return self.touchCache(key, value)

    def __setitem__(self, key, value):
        self.touchCache(key, value)

    def touchCache(self, key, value):
        self.cache[key] = value
        if value in self.cache_LRU:
            self.cache_LRU.remove(value)
        self.cache_LRU = self.cache_LRU[-(self.cacheSize-1):] + [ value ]
        return value


class Process_sender():

    @classmethod
    def start_sender(self):
        msg = 'Сообщение пришедшее один раз'
        schedule.every(1).minutes.do(Process_sender.send_pack, msg)
        # рандомное время
        # schedule.every(5).to(10).seconds.do(my_job)
        # если время по базе
        while True: #Запуск цикла
            schedule.run_pending()
            time.sleep(1)


    def send_pack(msg):
        from bot_main import bot
        bot.send_message(, msg)
        return schedule.CancelJob
