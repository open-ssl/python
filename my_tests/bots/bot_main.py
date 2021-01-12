# -*- coding: utf-8 -*-
import telebot
from telebot import types
import time
# import config
# ps aux | grep python
import sqlite3
from sql.classes import SQL_ConnectTable, SQL_EnglishWords_Table, \
                    SQL_UserTable, SQL_Main

token = ''
owner_id = int()
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
    connect_obj = SQL_Main(database_name)
    msg = keyboard = None
    if message.text == 'text':
        msg = 'Пока я не умею распознавать текст {}.Нужно пользоваться функциями)'.format(message.text)
    elif message.text == '/level1':
        words = connect_obj.select_word()
        connect_obj.close()
        msg = 'Из базы приехало -  {0} и {1}'.format(words[0][1], words[0][2])
    elif message.text == '/rename':
        sended_msg = bot.send_message(message.chat.id, 'Введи новое имя:')
        bot.register_next_step_handler(sended_msg, rename)
    elif message.text == '/start':
        connect_obj.add_new_user(message.chat.id, message.chat.first_name)
        # keyboard = types.InlineKeyboardMarkup()
        # url_button1 = types.InlineKeyboardButton(text="Да, это я", callback_data="name_true")
        # url_button2 = types.InlineKeyboardButton(text="Ввести своё имя", callback_data="name_false")
        # keyboard.add(url_button1)
        # keyboard.add(url_button2)
        msg = """Привет {}! Это бот, который поможет тебе изучать новые иностранные слова!\nИмя, доступное боту, всегда можно поменять командой /rename""".format(message.chat.first_name)
        bot.send_message(message.chat.id, msg, reply_markup=keyboard)
        time.sleep(2)
        msg = """Для корректной работы мне нужно знать твое время. Иначе жди сообщений посреди ночи)) Выбери нужный часовой пояс или введи с клавиатуры""".format(message.chat.first_name)
        time_input = bot.send_message(message.chat.id, msg, reply_markup=keyboard)
        # msg = """По умолчанию ты работаешь с уровнем 1 - команда /level1\nДля усложнения активируй /level2\n/info - вызов информации\nПриятного общения =)""".format(message.chat.first_name)
    elif message.text == '/info':
        msg = """Доступные команды:\nПервый уровень - /level1\nВторой уровень - /level2\n
        ss - Пауза. Слова будут спрашиваться через определенное время\nВызов информации - /info
        """
    else:
        msg = message.chat.id

    if msg:
        bot.send_message(message.chat.id, msg, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        connect_obj = SQL_Main(database_name)
        if call.data == "name_true":
            connect_obj.add_new_user(call.message.chat.id, call.message.chat.first_name)
            bot.send_message(call.message.chat.id, 'ok!')
        elif call.data == "name_false":
            bot.send_message(call.message.chat.id, 'Чтобы задать имя используй команду /rename')

def rename(message):
    chat_id, new_name = message.chat.id, message.text
    connect_obj = SQL_Main(database_name)
    connect_obj.rename_user(chat_id, new_name)
    bot.send_message(chat_id, f'Имя {new_name} установлено как текущее')


if __name__ == '__main__':
    # if int(time.strftime('%w')) not in
    bot.send_message(, 'bot started')
    print('bot started')
    bot.polling(none_stop=True)
