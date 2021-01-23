# -*- coding: utf-8 -*-
import sqlite3
from sql.classes import SQL_ConnectTable, SQL_EnglishWords_Table, \
                    SQL_UserTable

database_name = 'bot.db'

if __name__ == '__main__':
    # инициализируем слова
    e_words_table_obj = SQL_EnglishWords_Table(database_name)
    user_table_obj = SQL_UserTable(database_name)
    e_words_table_obj.set_level1()
    count_level1 = e_words_table_obj.get_level1_words_count()
    msg = 'В базе для level 1 лежит {} слов'.format(count_level1)
    e_words_table_obj.close()
    user_table_obj.close()
    print(msg)
