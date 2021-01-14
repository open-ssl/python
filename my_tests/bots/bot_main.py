# -*- coding: utf-8 -*-
import telebot
from telebot import types
import time
# import config
# ps aux | grep python
# ps -elf | grep python

import sqlite3
from sql.classes import SQL_ConnectTable, SQL_EnglishWords_Table, \
                    SQL_UserTable, SQL_Main, UserCache

token = '1000988391:AAHUIFhz-JFhWE2YcqPetaLUyk0WMUr2z8I'
owner_id = int(465146483)
database_name = 'bot.db'
choise_time_dict = {
    'UTC+2': 'Калининград UTC+2',
    'UTC+3': 'Москва UTC+3',
    'UTC+4': 'Самара UTC+4',
    'UTC+5': 'Екатеринбург UTC+5',
    'UTC+6': 'Омск UTC+6',
    'UTC+7': 'Новосибирск UTC+7',
    'UTC+8': 'Иркутск UTC+8',
    'UTC+9': 'Якутск UTC+9',
    'UTC+10': 'Владивосток UTC+10',
    'custom_UTC': 'Выбрать другой пояс'
}


bot = telebot.TeleBot(token)
cache = UserCache(2)
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
    elif message.text == '/users':
        connect_obj.get_all_user()
    elif message.text == '/rename':
        sended_msg = bot.send_message(message.chat.id, 'Введи новое имя:')
        bot.register_next_step_handler(sended_msg, rename)
    elif message.text == '/start':
        cache[message.chat.id] = 'start'
        connect_obj.add_new_user(message.chat.id, message.chat.first_name)
        msg = """Привет {}! Это бот, который поможет тебе изучать новые иностранные слова!\nИмя, доступное боту, всегда можно поменять командой /rename""".format(message.chat.first_name)
        bot.send_message(message.chat.id, msg, reply_markup=keyboard)
        time.sleep(2)
        keyboard = types.InlineKeyboardMarkup()
        for key in choise_time_dict:
            keyboard.add(types.InlineKeyboardButton(text=choise_time_dict[key], callback_data=key))
        msg = """Для корректной работы мне нужно знать твое время. Иначе жди сообщений посреди ночи)) Выбери нужный часовой пояс или введи с клавиатуры""".format(message.chat.first_name)
        bot.send_message(message.chat.id, msg, reply_markup=keyboard)
        keyboard = None
        while True:
            if cache[message.chat.id] == 'time_putted':
                bot.send_message(message.chat.id, 'Время установлено')
                msg = """По умолчанию ты работаешь с уровнем 1 - команда /level1\nДля усложнения активируй /level2\n/info - вызов информации\nПриятного общения =)""".format(message.chat.first_name)
                break
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
        if call.data in choise_time_dict:
            if call.data == 'custom_UTC':
                time_sended_msg = bot.send_message(call.message.chat.id, 'Введите время в формате UTC например "+4" или "-10"')
                bot.register_next_step_handler(time_sended_msg, set_time)
            else:
                connect_obj.set_user_time(call.message.chat.id, call.data[3:])
                bot.send_message(call.message.chat.id, f'Время {call.data[3:]} установлено ')
                cache[call.message.chat.id] = 'time_putted'
        # elif call.data == "name_false":
        #     bot.send_message(call.message.chat.id, 'Чтобы задать имя используй команду /rename')
        #     cache[call.message.chat.id] = 'time_putted'

def rename(message):
    chat_id, new_name = message.chat.id, message.text
    connect_obj = SQL_Main(database_name)
    connect_obj.rename_user(chat_id, new_name)
    bot.send_message(chat_id, f'Имя {new_name} установлено как текущее')

def set_time(message):
    chat_id, inputed_time = message.chat.id, message.text
    connect_obj = SQL_Main(database_name)
    try:
        if str(inputed_time) and len(inputed_time) > 1 and inputed_time[0] in ['+', '-'] and int(inputed_time[1:]):
            connect_obj.set_user_time(chat_id, inputed_time)
            bot.send_message(chat_id, f'Время {inputed_time} установлено')
            cache[call.message.chat.id] = 'time_putted'
    except:
        time_sended_msg = bot.send_message(chat_id, 'Введите время в формате UTC например "+4" или "-10"')
        bot.register_next_step_handler(time_sended_msg, set_time)


if __name__ == '__main__':
    # if int(time.strftime('%w')) not in
    bot.send_message(465146483, 'bot started')
    print('bot started')
    bot.polling(none_stop=True)
