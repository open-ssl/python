import sqlite3

class SQL_ConnectTable:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        # self.cursor = self.connection.cursor()
        # self.cursor.execute("""DROP TABLE IF EXISTS connect_table
        #            """)
        #
        # self.cursor.execute("""CREATE TABLE connect_table
        #           (connect_id integer, connect_name text)
        #        """)

    def ct_close(self):
        self.connection.close()




class SQL_EnglishWords_Table:

    def __init__(self, database):
        self.database = database
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""DROP TABLE IF EXISTS english_words_table
                   """)

        print('ew words table was created)))')
        self.cursor.execute("""CREATE TABLE english_words_table
                  (id integer, word text, translate text, sound text)
               """)

    def set_level1(self):
        with self.connection, \
            open('/Users/stanislavlukanov/Desktop/LEARN/python/python/my_tests/bots/en_words/level1.txt', 'r') as f:
            file = f.readlines()
            for row in file:
                word, translate = row.split(' ')
                print('ok')
                self.cursor.execute("INSERT INTO english_words_table VALUES(?, ?, ?, ?)", (1, word, translate, ' '))
                self.connection.commit()

    def get_level1_words_count(self):
        self.connection = sqlite3.connect(self.database)
        with self.connection:
            a = self.cursor.execute("""Select * from english_words_table""").fetchall()
            return len(a)

    def ew_close(self):
        self.connection.close()


class SQL_UserTable:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""DROP TABLE IF EXISTS user_table
                   """)

        self.cursor.execute("""CREATE TABLE user_table
                  (user_id integer, level_id integer user_name text)
               """)

    def ut_close(self):
        self.connection.close()
