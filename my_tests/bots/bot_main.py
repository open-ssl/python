import telebot
# import config
# ps aux | grep python
import sqlite3
from sql.classes import SQL_ConnectTable, SQL_EnglishWords_Table, \
                    SQL_UserTable

token = '1000988391:AAHUIFhz-JFhWE2YcqPetaLUyk0WMUr2z8I'
owner_id = int(465146483)
database_name = 'bot.db'

bot = telebot.TeleBot(token)

# Start
#
#
#
# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):
#     bot.send_message(message.chat.id, message.text)
#
#
# def generate_markup(right_answer, wrong_answers):
#     """
#     Создаем кастомную клавиатуру для выбора ответа
#     :param right_answer: Правильный ответ
#     :param wrong_answers: Набор неправильных ответов
#     :return: Объект кастомной клавиатуры
#     """
#     markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
#     # Склеиваем правильный ответ с неправильными
#     all_answers = '{},{}'.format(right_answer, wrong_answers)
#     # Создаем лист (массив) и записываем в него все элементы
#     list_items = []
#     for item in all_answers.split(','):
#         list_items.append(item)
#     # Хорошенько перемешаем все элементы
#     shuffle(list_items)
#     # Заполняем разметку перемешанными элементами
#     for item in list_items:
#         markup.add(item)
    # return markup

# finish

@bot.message_handler(content_types=["text"])
def text_handler(message): # Название функции не играет никакой роли, в принципе
    comment_no_words = f'Пока я не умею распознавать текст {message.text}. Нужно пользоваться функциями)'
    bot.send_message(message.chat.id, comment_no_words)

@bot.message_handler(commands=['level1'])
def command_hello(message):
    tmp = SQL_EnglishWords_Table(database_name)
    tmp.set_level()
    count_level1 = tmp.get_level1_words_count()
    msg = 'В базе для level 1 лежит {} слов'.format(count_level1)
    bot.send_message(message.chat.id, msg)
    tmp.ew_close()

if __name__ == '__main__':
    connect_table_obj = SQL_ConnectTable(database_name)
    connect_table_obj.ct_close()
    e_words_table_obj = SQL_EnglishWords_Table(database_name)
    e_words_table_obj.set_level1()
    level1_count = e_words_table_obj.get_level1_words_count()
    print("В таблице Level1 {} слов".format(level1_count))
    e_words_table_obj.ew_close()
    # user_table_obj = SQL_UserTable(database_name)
    # user_table_obj.ut_close()
    print('ok')

    bot.polling(none_stop=True)
