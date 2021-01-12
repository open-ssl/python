import sqlite3

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
             obj = self.cursor.execute('SELECT * FROM english_words_table').fetchall()
             return obj


    def add_new_user(self, chat_id, username):
        with self.connection:
            print('chat_id!!!')
            print(chat_id)
            # (user_id integer, level_id integer user_name text)
            # obj = self.cursor.execute("SELECT 1 FROM user_table WHERE user_id = ?", chat_id)
            obj = self.cursor.execute('SELECT * FROM user_table WHERE user_id = ?', (chat_id,)).fetchall()
            if not obj:
                self.cursor.execute("INSERT INTO user_table VALUES(?, ?, ?)", (chat_id, 1, username))
                self.connection.commit()
                print('ADDED USER IN TABLE')


    def rename_user(self, chat_id, new_username):
        with self.connection:
             # (user_id integer, level_id integer user_name text)
            self.cursor.execute("UPDATE user_table SET user_name = ? where user_id = ?", (new_username, chat_id, ))
            self.connection.commit()
            print('RENAME USER IN TABLE')

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




class SQL_EnglishWords_Table:

    def __init__(self, database=None):
        if not database:
            return
        self.database = database
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""DROP TABLE IF EXISTS english_words_table
                   """)

        self.cursor.execute("""CREATE TABLE english_words_table
                  (id integer, word text, translate text, sound text)
               """)
        print('ew words table was created)))')


    def set_level1(self):
        with self.connection, \
            open('/Users/stanislavlukanov/Desktop/LEARN/python/python/my_tests/bots/en_words/level1.txt', 'r') as f:
            file = f.readlines()
            for it, row in enumerate(file):
                word, translate = row.split(' ')
                self.cursor.execute("INSERT INTO english_words_table VALUES(?, ?, ?, ?)", (it, word, translate, ' '))
                self.connection.commit()
            print('LEVEL 1 WAS CREATED')


    def get_level1_words_count(self):
        "Смотрим сколько записей в таблице"
        self.connection = sqlite3.connect(self.database)
        with self.connection:
            a = self.cursor.execute("""Select * from english_words_table""").fetchall()
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
                  (user_id integer, level_id integer, user_name text)
               """)

    def close(self):
        self.connection.close()
